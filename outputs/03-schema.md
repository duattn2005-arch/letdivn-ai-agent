# Schema Markup — letsdoitvietnam.org

*Skill: `schema` · Hiện trạng: không tìm thấy JSON-LD trong HTML của 43/43 trang (`data/web/pages.csv`, cột `schema_types`). Cần kiểm tra lại bằng Rich Results Test vì có thể có schema chèn bằng JavaScript.*

Cách gắn trên WordPress: cài Rank Math hoặc Yoast (tự sinh Organization, Article, BreadcrumbList), rồi dán thêm Event bằng plugin "Insert Headers and Footers" hoặc trường tùy chỉnh trên trang sự kiện.

## 1. Trang chủ — NGO (Organization)

```json
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "name": "Let's Do It Vietnam",
  "alternateName": "Let's do it! Vietnam",
  "url": "https://letsdoitvietnam.org/",
  "logo": "https://letsdoitvietnam.org/wp-content/plugins/ldivn-cleanup-map-off/assets/images/logo-footer.png",
  "description": "Let's Do It Vietnam is the World Cleanup Day movement in Vietnam, bringing volunteers, partners and communities together for a clean planet.",
  "foundingDate": "2015",
  "email": "letsdoitvietnam@gmail.com",
  "telephone": "+84358726755",
  "areaServed": { "@type": "Country", "name": "Vietnam" },
  "parentOrganization": { "@type": "NGO", "name": "Let's Do It World", "url": "https://letsdoitworld.org/" },
  "sameAs": [
    "https://www.facebook.com/LetsDoItVietNam",
    "https://www.instagram.com/letsdoitvietnam/"
  ]
}
```

## 2. Trang sự kiện — Event (ví dụ World Cleanup Day 2026, Hà Nội)

Điền đúng ngày, địa điểm của từng sự kiện; không gắn Event cho sự kiện không có ngày cụ thể.

```json
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "World Cleanup Day 2026 – Hà Nội",
  "startDate": "2026-09-20T07:00:00+07:00",
  "endDate": "2026-09-20T11:00:00+07:00",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "location": {
    "@type": "Place",
    "name": "[TÊN ĐỊA ĐIỂM]",
    "address": { "@type": "PostalAddress", "addressLocality": "Hà Nội", "addressCountry": "VN" }
  },
  "image": ["[URL ẢNH 1200x630]"],
  "description": "Ngày hội dọn rác World Cleanup Day tại Hà Nội — giảm rác nhựa tại nguồn và thúc đẩy kinh tế tuần hoàn.",
  "isAccessibleForFree": true,
  "organizer": { "@type": "NGO", "name": "Let's Do It Vietnam", "url": "https://letsdoitvietnam.org/" },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "VND",
    "availability": "https://schema.org/InStock",
    "url": "https://letsdoitvietnam.org/join-us/"
  }
}
```

## 3. Bài viết — NewsArticle + BreadcrumbList

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "NewsArticle",
      "headline": "Let's Do It Vietnam X The Body Shop: Community Cleanup in Hai Phong",
      "datePublished": "2026-10-22T14:49:38+07:00",
      "image": ["[URL ẢNH ĐẠI DIỆN]"],
      "author": { "@type": "Organization", "name": "Let's Do It Vietnam" },
      "publisher": { "@type": "NGO", "name": "Let's Do It Vietnam", "url": "https://letsdoitvietnam.org/" },
      "mainEntityOfPage": "https://letsdoitvietnam.org/2026/10/22/lets-do-it-vietnam-x-the-body-shop-community-cleanup-in-hai-phong/"
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://letsdoitvietnam.org/" },
        { "@type": "ListItem", "position": 2, "name": "News", "item": "https://letsdoitvietnam.org/news/" },
        { "@type": "ListItem", "position": 3, "name": "Community Cleanup in Hai Phong" }
      ]
    }
  ]
}
```

## 4. Trang /faq/ — FAQPage
Google chỉ còn hiển thị FAQ rich result cho trang chính phủ/y tế, nhưng FAQPage vẫn giúp AI đọc hiểu nội dung (xem `04-ai-seo.md`). Nội dung câu hỏi lấy từ file đó.

## Testing Checklist
- [ ] Event và Article là tính năng Google còn hỗ trợ; NGO/Organization dùng cho Knowledge Panel
- [ ] Dán từng đoạn vào https://validator.schema.org/ và https://search.google.com/test/rich-results
- [ ] Sửa hết lỗi bắt buộc, xem lại cảnh báo
- [ ] Nội dung schema khớp nội dung hiển thị trên trang (ngày, địa điểm, tiêu đề)
- [ ] Thay mọi chỗ `[...]` bằng dữ liệu thật trước khi đăng
