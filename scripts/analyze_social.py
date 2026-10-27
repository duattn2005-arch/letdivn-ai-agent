"""Phân tích dữ liệu Facebook (Meta Business Suite) và TikTok (TikTok Studio).

Bỏ file CSV xuất từ hai nền tảng vào data/facebook/ và data/tiktok/, rồi chạy:
    python scripts/analyze_social.py
Đầu ra: outputs/social-report.md

Tên cột được nhận diện theo từ khóa (tiếng Anh hoặc tiếng Việt), nên không cần sửa file xuất.
"""
import csv
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if len(sys.argv) > 1:  # cho phép chỉ định thư mục dữ liệu khác khi thử nghiệm
    ROOT = Path(sys.argv[1]).resolve()
OUT = ROOT / "outputs" / "social-report.md"

# Mỗi trường: danh sách từ khóa, khớp nếu tên cột chứa một từ khóa (không phân biệt hoa thường)
FIELDS = {
    "time": ["publish time", "post time", "time posted", "created", "thời gian đăng", "ngày đăng", "date"],
    "text": ["description", "title", "message", "caption", "video title", "mô tả", "tiêu đề", "nội dung"],
    "type": ["post type", "loại bài viết", "type"],
    "reach": ["reach", "views", "video views", "lượt tiếp cận", "lượt xem", "impressions", "lượt hiển thị"],
    "reactions": ["reactions", "likes", "cảm xúc", "lượt thích"],
    "comments": ["comments", "bình luận"],
    "shares": ["shares", "chia sẻ"],
    "link": ["permalink", "link", "url", "liên kết"],
}
WEEKDAYS = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]


def map_columns(headers):
    mapping = {}
    for field, keys in FIELDS.items():
        for key in keys:
            col = next((h for h in headers if key in h.lower() and h not in mapping.values()), None)
            if col:
                mapping[field] = col
                break
    return mapping


def num(value):
    try:
        return float(str(value).replace(",", "").replace(".", "").strip() or 0)
    except ValueError:
        return 0.0


def parse_time(value):
    value = (value or "").strip()
    for fmt in ("%m/%d/%Y %H:%M", "%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value[:len(datetime.now().strftime(fmt))], fmt)
        except ValueError:
            continue
    return None


def load(platform):
    rows = []
    for path in sorted((ROOT / "data" / platform).glob("*.csv")):
        with open(path, encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            mapping = map_columns(reader.fieldnames or [])
            for r in reader:
                post = {k: r.get(c, "") for k, c in mapping.items()}
                for k in ("reach", "reactions", "comments", "shares"):
                    post[k] = num(post.get(k))
                post["when"] = parse_time(post.get("time"))
                post["engagement"] = post["reactions"] + post["comments"] + post["shares"]
                rows.append(post)
    return rows


def report(platform, label, posts):
    if not posts:
        return [f"## {label}\n", f"Chưa có dữ liệu. Xem hướng dẫn tải ở data/{platform}/README.md.\n"]
    total_reach = sum(p["reach"] for p in posts)
    total_eng = sum(p["engagement"] for p in posts)
    rate = total_eng / total_reach * 100 if total_reach else 0
    dated = [p["when"] for p in posts if p["when"]]
    span = f"{min(dated):%d/%m/%Y} – {max(dated):%d/%m/%Y}" if dated else "không rõ"
    lines = [
        f"## {label}\n",
        f"- Số bài: **{len(posts)}** (giai đoạn {span})",
        f"- Tổng lượt tiếp cận/xem: **{total_reach:,.0f}**, trung bình **{total_reach / len(posts):,.0f}**/bài",
        f"- Tổng tương tác (cảm xúc + bình luận + chia sẻ): **{total_eng:,.0f}**",
        f"- Tỷ lệ tương tác: **{rate:.2f}%** (tương tác ÷ tiếp cận)\n",
        "### Top 5 bài theo tương tác\n",
        "| # | Ngày | Nội dung | Tiếp cận | Tương tác |",
        "| --- | --- | --- | --- | --- |",
    ]
    for i, p in enumerate(sorted(posts, key=lambda p: p["engagement"], reverse=True)[:5], 1):
        text = " ".join((p.get("text") or "").split())[:70].replace("|", "/")
        day = f"{p['when']:%d/%m/%Y}" if p["when"] else ""
        lines.append(f"| {i} | {day} | {text} | {p['reach']:,.0f} | {p['engagement']:,.0f} |")

    by_day = defaultdict(list)
    for p in posts:
        if p["when"]:
            by_day[p["when"].weekday()].append(p["engagement"])
    if by_day:
        lines += ["\n### Tương tác trung bình theo ngày đăng\n", "| Ngày | Số bài | TB tương tác |", "| --- | --- | --- |"]
        for d in sorted(by_day, key=lambda d: -sum(by_day[d]) / len(by_day[d])):
            v = by_day[d]
            lines.append(f"| {WEEKDAYS[d]} | {len(v)} | {sum(v) / len(v):,.1f} |")

    by_type = defaultdict(list)
    for p in posts:
        if p.get("type"):
            by_type[p["type"]].append(p)
    if len(by_type) > 1:
        lines += ["\n### Theo loại bài\n", "| Loại | Số bài | TB tiếp cận | TB tương tác |", "| --- | --- | --- | --- |"]
        for t, v in sorted(by_type.items(), key=lambda kv: -sum(p["engagement"] for p in kv[1]) / len(kv[1])):
            lines.append(f"| {t} | {len(v)} | {sum(p['reach'] for p in v) / len(v):,.0f} | "
                         f"{sum(p['engagement'] for p in v) / len(v):,.1f} |")
    return lines + [""]


if __name__ == "__main__":
    parts = ["# Báo cáo dữ liệu mạng xã hội\n",
             f"Tạo tự động bởi scripts/analyze_social.py lúc {datetime.now():%d/%m/%Y %H:%M}.\n"]
    parts += report("facebook", "Facebook", load("facebook"))
    parts += report("tiktok", "TikTok", load("tiktok"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Đã ghi {OUT.relative_to(ROOT)}")
