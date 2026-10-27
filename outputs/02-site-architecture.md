# Site Architecture — letsdoitvietnam.org

*Skill: `site-architecture` · Dữ liệu: `data/web/pages.csv` (18 trang tĩnh + 25 bài viết).*

## Vấn đề hiện tại
- Bài viết dùng URL có ngày: `/2026/10/22/lets-do-it-vietnam-x-the-body-shop-.../`. URL dài, nhìn là biết bài cũ.
- 25/25 bài nằm trong "Uncategorized", nên không có trang tổng hợp theo chủ đề.
- Trang chương trình (World Cleanup Day, Green Ocean, YCSW…) không liên kết sang các bài viết cùng chủ đề.
- Có trang thừa `/sample-page/` và trang trùng `/contact/` – `/contact-us/`.

## Cấu trúc đề xuất

```
/                                   Trang chủ
├── /who-we-are/                    Giới thiệu
├── /our-team/
├── /our-partners/                  + /partner-with-us/ (MỚI: trang dành cho doanh nghiệp)
├── /programs/                      Hub chương trình (MỚI, thay /what-we-do/)
│   ├── /programs/world-cleanup-day/
│   ├── /programs/green-ocean-campaign/
│   ├── /programs/community-workshop/
│   ├── /programs/environmental-day/
│   ├── /programs/ycsw/
│   └── /programs/cigarette-butts/
├── /join-us/                       Đăng ký tình nguyện viên
├── /cleanup-map/                   Bản đồ điểm dọn rác
├── /news/                          Tin tức, lọc theo chuyên mục
│   ├── /news/category/su-kien-don-rac/
│   ├── /news/category/doi-tac/
│   ├── /news/category/giao-duc-moi-truong/
│   ├── /news/category/song-xanh/
│   └── /news/{slug}/               Bài viết (bỏ ngày tháng)
├── /media-coverage/
├── /faq/                           MỚI: câu hỏi thường gặp (phục vụ ai-seo)
└── /contact/                       (/contact-us/ → 301 về đây)
```

## Quy tắc URL (áp dụng cho mọi bài mới)
- Settings → Permalinks → Custom: `/news/%postname%/`. Từ đó mỗi bài đăng mới tự có URL đúng chuẩn.
- Slug: chữ thường, không dấu, nối bằng gạch ngang, tối đa 5–6 từ. Ví dụ: `/news/body-shop-cleanup-do-son-hai-phong/`.
- Trước khi đổi permalink, tạo chuyển hướng 301 từ dạng cũ `/%year%/%monthnum%/%day%/%postname%/` sang dạng mới (plugin Redirection làm tự động).

## Menu chính (≤ 7 mục)
`Giới thiệu · Chương trình · Bản đồ dọn rác · Tin tức · Đối tác · Liên hệ` + nút nổi bật **Tham gia ngay** → `/join-us/`.

## Liên kết nội bộ
| Từ trang | Liên kết đến |
| --- | --- |
| Mỗi bài sự kiện | Trang chương trình tương ứng + `/cleanup-map/` + `/join-us/` |
| Trang chương trình | 3 bài mới nhất cùng chuyên mục |
| Bài về đối tác | `/partner-with-us/` |
| Trang chủ | `/cleanup-map/`, `/join-us/`, 3 bài mới nhất |

Breadcrumb trên mọi trang con: `Trang chủ › Tin tức › Tên bài` (kèm schema BreadcrumbList, xem `03-schema.md`).
