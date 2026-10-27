# SEO Audit — letsdoitvietnam.org

*Skill: `seo-audit` · Dữ liệu: `data/web/pages.csv` (43 URL từ sitemap), `data/web/posts.csv` (25 bài), quét ngày 27/10/2026 bằng `scripts/crawl_web.py`.*

## Executive Summary

Website được Google thu thập tốt (sitemap đầy đủ, robots.txt mở, mọi trang trả mã 200, có canonical). Phần yếu nằm ở **on-page**: không trang nào có meta description, 96% ảnh thiếu alt, 15 trang không có thẻ H1, bài viết ngắn và đều nằm trong mục "Uncategorized".

| Chỉ số | Kết quả | Mục tiêu |
| --- | --- | --- |
| Trang có meta description | 0/43 | 43/43 |
| Ảnh có alt text | 17/451 (4%) | > 90% |
| Trang có đúng 1 H1 | 28/43 | 43/43 |
| Title dài hơn 60 ký tự | 23/43 | 0 |
| Trang có og:image (ảnh khi chia sẻ Facebook) | 0/43 | 43/43 |
| Schema JSON-LD trong HTML | 0/43 | Trang chủ, bài viết, sự kiện |
| Thời gian tải HTML (trung vị / tối đa) | 1.061 ms / 1.839 ms | < 800 ms |
| Bài viết dưới 300 từ | 18/25 | < 5 |
| Bài có chuyên mục | 0/25 (tất cả "Uncategorized") | 25/25 |

**Top 5 việc ưu tiên**
1. Viết meta description cho 43 trang (quick win, 1–2 giờ với plugin SEO).
2. Thêm alt text cho ảnh, bắt đầu từ trang chủ (33 ảnh thiếu) và bài sự kiện.
3. Thêm H1 cho 15 trang tĩnh (Who We Are, What We Do, Join Us…).
4. Gắn og:image để bài chia sẻ lên Facebook có ảnh đẹp — quan trọng vì Facebook là kênh chính.
5. Phân chuyên mục bài viết và viết dài hơn cho bài sự kiện (xem `06-content-strategy.md`).

## Technical SEO Findings

**1. Không có og:image / Open Graph**
- Impact: Cao (với kênh Facebook) · Priority: High
- Evidence: cột `og_image` = "no" ở 43/43 trang.
- Fix: cài Yoast SEO hoặc Rank Math, đặt ảnh mặc định 1200×630 và ảnh đại diện cho từng bài.

**2. Trang thừa và trùng lặp**
- Impact: Trung bình · Priority: Medium
- Evidence: `/sample-page/` (trang mẫu mặc định của WordPress) vẫn có trong sitemap; `/contact/` và `/contact-us/` cùng chức năng.
- Fix: xóa `/sample-page/`; giữ `/contact/`, chuyển hướng 301 `/contact-us/` → `/contact/`.

**3. Thời gian phản hồi HTML ~1 giây**
- Impact: Trung bình · Priority: Medium
- Evidence: `load_ms` trung vị 1.061 ms, chậm nhất 1.839 ms (bài Leaders Academy, LAM Project).
- Fix: bật cache trang (LiteSpeed Cache / WP Super Cache), nén ảnh sang WebP. Đo lại bằng PageSpeed Insights để có Core Web Vitals.

**4. Ngôn ngữ khai báo en-US cho nội dung có tiếng Việt**
- Impact: Thấp–Trung bình · Priority: Low
- Evidence: 43/43 trang `lang="en-US"`, nhưng 4 bài có tiêu đề tiếng Việt và trang Join Us có nút "Đơn đăng ký".
- Fix: ngắn hạn giữ tiếng Anh nhất quán trên trang; dài hạn làm bản tiếng Việt riêng (`/vi/`) với hreflang.

**5. URL bài viết có ngày tháng**
- Impact: Thấp · Priority: Low
- Evidence: dạng `/2026/10/22/ten-bai/`.
- Fix: chuyển permalink sang `/news/ten-bai/` khi tái cấu trúc (cần 301 cho URL cũ) — xem `02-site-architecture.md`.

## On-Page SEO Findings

**6. Không có meta description**
- Impact: Cao · Priority: High
- Evidence: `desc_len` = 0 ở 43/43 trang. Google sẽ tự cắt một đoạn bất kỳ, thường là chữ của menu.
- Fix: viết 120–155 ký tự cho mỗi trang, có từ khóa và lời kêu gọi. Bản mẫu cho 10 trang chính ở `07-copywriting.md`.

**7. Title quá dài**
- Impact: Trung bình · Priority: Medium
- Evidence: 23/43 title > 60 ký tự, dài nhất 136 ký tự (bài World Cleanup Day 2026 Hà Nội). Nhiều title viết HOA toàn bộ.
- Fix: rút còn ≤ 60 ký tự, đưa từ khóa lên đầu, bỏ viết hoa toàn bộ.

**8. Trang không có H1**
- Impact: Trung bình · Priority: High
- Evidence: `h1_count` = 0 ở 15 trang, gồm trang chủ, Who We Are, What We Do, Our Partners, Join Us, World Cleanup Day, News.
- Fix: đổi tiêu đề lớn đầu trang (đang là H2 hoặc chữ trong module Divi) thành H1.

**9. Ảnh thiếu alt**
- Impact: Trung bình (SEO ảnh + khả năng truy cập) · Priority: Medium
- Evidence: 434/451 ảnh không có alt. Trang chủ 33/36, YCSW 27/27, Our Partners 24/24.
- Fix: logo đối tác → alt = tên đối tác; ảnh sự kiện → mô tả "Tình nguyện viên dọn rác tại biển Đồ Sơn, Hải Phòng".

## Content Findings

**10. Bài viết mỏng**
- Impact: Cao · Priority: High
- Evidence: phần thân 18/25 bài dưới 300 từ; trung vị 154 từ; bài mới nhất (The Body Shop) 105 từ, không có số liệu kg rác hay số người tham gia.
- Fix: mỗi bài sự kiện theo khung: ở đâu – khi nào – bao nhiêu người – bao nhiêu kg rác – loại rác chính – trích lời – ảnh – lời mời tham gia lần sau. Mục tiêu 500+ từ.

**11. Không phân chuyên mục**
- Impact: Trung bình · Priority: Medium
- Evidence: 25/25 bài thuộc "Uncategorized".
- Fix: tạo 4 chuyên mục theo content pillar (`06-content-strategy.md`), gán lại 25 bài.

**12. Tín hiệu E-E-A-T còn yếu**
- Impact: Trung bình · Priority: Low
- Evidence: bài không có tác giả, không dẫn nguồn số liệu.
- Fix: thêm tên tác giả/điều phối viên, dẫn số liệu từ báo cáo World Cleanup Day.

## Prioritized Action Plan

1. **Critical:** không có lỗi chặn index.
2. **High-impact:** meta description (43 trang) · H1 (15 trang) · og:image · viết lại bài sự kiện theo khung.
3. **Quick wins:** xóa `/sample-page/` · 301 `/contact-us/` · rút gọn 23 title · alt cho logo đối tác.
4. **Long-term:** chuyên mục + permalink `/news/` · bản tiếng Việt `/vi/` · schema (`03-schema.md`) · llms.txt (`04-ai-seo.md`).

> Giới hạn: theo skill `seo-audit`, curl không thấy schema do JavaScript chèn vào. Cần kiểm tra lại bằng Google Rich Results Test trước khi kết luận "không có schema". Chưa có dữ liệu Google Search Console, nên audit chưa có thứ hạng và lượt nhấp.
