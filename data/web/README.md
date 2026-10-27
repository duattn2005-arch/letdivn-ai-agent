# Dữ liệu website — letsdoitvietnam.org

## Đã có (tải tự động)
| File | Nội dung | Tạo bởi |
| --- | --- | --- |
| `pages.csv` | 43 URL trong sitemap: mã trạng thái, thời gian tải, title, meta description, H1, số từ, ảnh thiếu alt, liên kết nội bộ, canonical, og:image, schema | `python scripts/crawl_web.py` |
| `posts.csv` | 25 bài viết từ WordPress REST API: ngày, tiêu đề, URL, chuyên mục, số từ phần thân | cùng script |

Quét lần cuối: 27/10/2026. Chạy lại script bất cứ lúc nào để cập nhật.

## Nên tải thêm (cần quyền quản trị website)
**Google Search Console** (từ khóa và lượt nhấp):
1. https://search.google.com/search-console → chọn property letsdoitvietnam.org.
2. **Hiệu suất** → **Kết quả tìm kiếm** → chọn 3 tháng.
3. Bấm **Xuất** → **Tải xuống CSV**. Giải nén và lưu `Queries.csv`, `Pages.csv` vào đây với tên `gsc-queries.csv`, `gsc-pages.csv`.

**Google Analytics 4** (lượt truy cập, nguồn, chuyển đổi):
1. https://analytics.google.com → **Báo cáo** → **Thu nạp lưu lượng truy cập** (Traffic acquisition).
2. Biểu tượng chia sẻ (góc trên phải) → **Tải tệp xuống** → **CSV**. Lưu thành `ga4-traffic.csv`.
3. Làm tương tự với **Trang và màn hình** (Pages and screens) → `ga4-pages.csv`.

**PageSpeed Insights** (tốc độ thực tế): https://pagespeed.web.dev → nhập trang chủ → chụp màn hình kết quả, lưu `pagespeed-home.png`.

Có dữ liệu Search Console thì gửi file cho agent kèm câu: "Dùng skill seo-audit, tìm từ khóa đang ở vị trí 8–20 để đẩy lên trang 1".
