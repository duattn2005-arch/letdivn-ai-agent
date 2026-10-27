# Dữ liệu Facebook — fanpage fb.com/LetsDoItVietNam

Cần quyền quản trị (admin hoặc editor) của fanpage.

## Cách tải
1. Vào https://business.facebook.com và chọn trang **Let's Do It Vietnam**.
2. Menu trái: **Thông tin chi tiết** (Insights) → **Nội dung** (Content).
3. Chọn khoảng thời gian (gợi ý: 90 ngày gần nhất, hoặc 01/07 – 31/10 để bao trọn World Cleanup Day).
4. Bấm **Xuất dữ liệu** (Export data) → chọn **Bài viết** (Posts) → định dạng **CSV**.
5. Lưu file vào thư mục này, ví dụ `facebook-posts-2026-q3.csv`.

Nếu không có quyền admin: nhờ người quản lý page tải giúp, hoặc dùng Meta Business Suite → Insights → "Tải xuống báo cáo" và gửi bạn file.

## Cột script cần (tự nhận diện, tiếng Anh hoặc tiếng Việt)
Thời gian đăng · Mô tả/Tiêu đề · Loại bài · Lượt tiếp cận · Cảm xúc · Bình luận · Lượt chia sẻ.

## Sau khi có file
```
python scripts/analyze_social.py
```
→ kết quả ở `outputs/social-report.md`.
