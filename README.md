# LetDIVN Marketing Agent

AI agent làm marketing cho website **Let's Do It Vietnam** (https://letsdoitvietnam.org). Agent được xây từ **10 skill** chọn trong bộ [marketingskills](https://github.com/coreyhaines31/marketingskills), dùng dữ liệu thật của website và mạng xã hội.

## Agent gồm những gì

```
letdivn-ai-agent/
├── skills/            10 skill (kiến thức chuyên môn mà agent làm theo)
├── context/           Hồ sơ thương hiệu — mọi skill đọc file này trước
├── data/
│   ├── web/           Dữ liệu website (đã tải: 43 trang, 25 bài viết)
│   ├── facebook/      Dữ liệu fanpage (xuất từ Meta Business Suite)
│   └── tiktok/        Dữ liệu TikTok (xuất từ TikTok Studio, nếu dùng)
├── scripts/           Script tải và phân tích dữ liệu
├── outputs/           Kết quả agent chạy trên dữ liệu
└── prompts/           Prompt để dùng agent trên ChatGPT
```

## 10 skill đã chọn

**Loại 1 — dùng trực tiếp cho website** (agent đọc dữ liệu web và sửa site)

| # | Skill | Việc làm cho website | Kết quả |
| --- | --- | --- | --- |
| 1 | seo-audit | Kiểm tra SEO 43 trang | [01-seo-audit.md](outputs/01-seo-audit.md) |
| 2 | site-architecture | Cấu trúc menu, URL tự động cho bài mới | [02-site-architecture.md](outputs/02-site-architecture.md) |
| 3 | schema | Dữ liệu cấu trúc NGO, Event, NewsArticle | [03-schema.md](outputs/03-schema.md) |
| 4 | ai-seo | Được ChatGPT/Gemini trích dẫn, llms.txt | [04-ai-seo.md](outputs/04-ai-seo.md), [llms.txt](outputs/llms.txt) |
| 5 | cro | Tăng đăng ký tình nguyện viên trang Join Us | [05-cro-join-us.md](outputs/05-cro-join-us.md) |

**Loại 2 — dùng cho AI làm content**

| # | Skill | Việc làm | Kết quả |
| --- | --- | --- | --- |
| 6 | product-marketing | Hồ sơ thương hiệu (nền cho mọi skill) | [product-marketing.md](context/product-marketing.md) |
| 7 | content-strategy | Content pillar, chấm điểm chủ đề, lịch 60/30/10 | [06-content-strategy.md](outputs/06-content-strategy.md) |
| 8 | copywriting | Title, meta description, hero trang chủ | [07-copywriting.md](outputs/07-copywriting.md) |
| 9 | social | Một bài web thành post Facebook, Instagram, TikTok | [08-social.md](outputs/08-social.md) |
| 10 | public-relations | Thông cáo báo chí, email gửi phóng viên | [09-public-relations.md](outputs/09-public-relations.md) |

**Vì sao không chọn các skill còn lại:** bộ gốc có 51 skill, nhiều skill dành cho doanh nghiệp bán hàng (pricing, paywalls, cold-email, churn-prevention, aso…). Let's Do It Vietnam là tổ chức phi lợi nhuận, cần tình nguyện viên và đối tác chứ không bán sản phẩm, nên các skill đó không phù hợp.

## Phát hiện chính từ dữ liệu website (27/10/2026)
- 0/43 trang có meta description; 0/43 có og:image (ảnh khi chia sẻ Facebook).
- 434/451 ảnh thiếu alt; 15 trang không có H1.
- 25/25 bài viết nằm trong "Uncategorized"; 18/25 bài dưới 300 từ.
- Có khoảng 5 tháng liền (04–08/2026) không đăng bài nào.
- Trang Join Us chỉ có 1 địa điểm, không có form ngay trên trang.

## Cách chạy

**Cài đặt:** Python 3.10+ (không cần thư viện ngoài). Agent chạy trên Claude Code, Antigravity, Cursor (đọc thư mục `skills/`) hoặc ChatGPT Project (xem `prompts/`).

```bash
# 1. Tải dữ liệu website
python scripts/crawl_web.py

# 2. Bỏ file CSV Facebook/TikTok vào data/facebook, data/tiktok (xem README trong mỗi thư mục), rồi:
python scripts/analyze_social.py
```

**Dùng agent trong Claude Code:** chép `skills/` vào `.claude/skills/` (Antigravity/Cursor: `.agents/skills/`), rồi ra lệnh, ví dụ:
- "Dùng seo-audit, đọc data/web/pages.csv và cập nhật outputs/01-seo-audit.md"
- "Dùng content-strategy với data/web/posts.csv và outputs/social-report.md, lập lịch tháng 11"

**Dùng trên ChatGPT:** xem [prompts/chatgpt-project.md](prompts/chatgpt-project.md).

## Việc còn thiếu
- [ ] Tải dữ liệu Facebook → `data/facebook/` rồi chạy `analyze_social.py`
- [ ] Tải dữ liệu TikTok (nếu có) → `data/tiktok/`
- [ ] (Tùy chọn) Google Search Console, GA4 → `data/web/` (xem `data/web/README.md`)
- [ ] Ban tổ chức xác nhận các chỗ `[...]` trong outputs trước khi đăng

## Nguồn và giấy phép
Skill lấy từ [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (commit `17772c7`, 26/10/2026), giấy phép MIT — xem `skills/LICENSE-marketingskills`. Bản fork [mysticaltech/marketingskills](https://github.com/mysticaltech/marketingskills) có cùng nội dung, đóng gói sẵn file `.skill`.
