# CRO — trang Join Us (đăng ký tình nguyện viên)

*Skill: `cro` · Trang: https://letsdoitvietnam.org/join-us/ · Mục tiêu chuyển đổi: người xem bấm đăng ký và gửi form.*

## Những gì trang đang có (quét ngày 27/10/2026)
- Đầu trang lặp lại danh sách 5 bài tin tức, **hai lần**, trước cả nội dung chính.
- Không có thẻ H1.
- Đoạn giới thiệu World Cleanup Day: đủ thông tin nhưng dài và nghe như văn bản hành chính.
- Chỉ có **một** địa điểm (Da Nang), kèm hai nút tiếng Việt "Đơn đăng ký" và "Link chi tiết bài đăng" trên một trang tiếng Anh.
- Không có form ngay trên trang; người xem phải sang trang khác.
- Không có số liệu tạo tin tưởng (số tình nguyện viên, số kg rác), ảnh người thật hay lời chứng thực.

## Đánh giá theo khung CRO
| Yếu tố | Hiện tại | Vấn đề |
| --- | --- | --- |
| Đề xuất giá trị (5 giây đầu) | Danh sách tin tức | Người xem không biết trang này để làm gì |
| Lời kêu gọi chính | 2 nút cạnh nhau, tên mơ hồ | Không rõ bấm nút nào |
| Bằng chứng | Không có | Thiếu lý do để tin và tham gia |
| Trở ngại | Sang trang khác để đăng ký | Mất người ở mỗi bước chuyển |
| Lựa chọn địa điểm | 1 thành phố | Người ở Hà Nội, TP.HCM thoát trang |

## Đề xuất (theo thứ tự tác động)
1. **Bỏ danh sách tin tức ở đầu trang.** Thay bằng H1 + một câu + nút:
   - H1: *Join the next cleanup near you*
   - Phụ đề: *[X] hours, free, tools provided. 300+ volunteers joined us in Hanoi at World Cleanup Day 2025.* (thời lượng, miễn phí, dụng cụ: xác nhận với ban tổ chức trước khi đăng)
   - Nút: **Find a cleanup near me** → `/cleanup-map/`
2. **Nhúng form ngắn ngay trên trang:** họ tên, email/Zalo, thành phố (danh sách chọn), vai trò (Tham gia / Tự tổ chức). Tối đa 4 trường; hỏi thêm sau khi đã đăng ký.
3. **Một nút chính, một nút phụ.** "Register" là nút chính; "Event details" là liên kết chữ nhỏ.
4. **Thêm dải số liệu** ngay dưới form: 1M+ volunteers · 100+ events · 40+ tons collected with VinUniversity (2025).
5. **Thêm 3 ảnh thật và 1 câu trích lời** của tình nguyện viên.
6. **Mục "What to expect"** gồm 3 dòng: thời gian, cần mang gì, ai hướng dẫn. Mục này trả lời trước lo ngại "có an toàn không".
7. **Thống nhất ngôn ngữ** của trang (tiếng Anh), hoặc làm bản tiếng Việt riêng.

## Ý tưởng A/B test
| Test | Bản A | Bản B | Chỉ số |
| --- | --- | --- | --- |
| Tiêu đề | "Join Us: 20 September – World Cleanup Day" | "Join the next cleanup near you" | % bấm nút chính |
| Vị trí form | Trang riêng | Nhúng trên trang | % gửi form |

## Đo lường
Gắn sự kiện GA4 `volunteer_signup` khi gửi form thành công và `map_register_click` khi bấm "Register to Join" trên bản đồ. Đây là 2 chỉ số chính để biết các thay đổi trên có hiệu quả không.
