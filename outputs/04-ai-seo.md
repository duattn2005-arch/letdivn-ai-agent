# AI SEO — để ChatGPT, Gemini, Perplexity nhắc đến Let's Do It Vietnam

*Skill: `ai-seo` · Kiểm tra ngày 27/10/2026.*

## Hiện trạng
| Hạng mục | Kết quả | Đánh giá |
| --- | --- | --- |
| robots.txt | `User-agent: *` chỉ chặn `/wp-admin/` | Tốt: mọi bot AI (OAI-SearchBot, PerplexityBot, Claude-SearchBot…) đều vào được |
| llms.txt | 404 — chưa có | Nên thêm (bản nháp bên dưới) |
| Schema | Không thấy trong HTML | Thêm NGO, Event, NewsArticle (`03-schema.md`) |
| Nội dung dễ trích dẫn | Bài ngắn (trung vị 154 từ), ít số liệu trong thân bài | Cần đoạn trả lời trực tiếp + số liệu |
| Trang FAQ | Chưa có | Thêm `/faq/` |

## Bước 1 — Câu hỏi cần kiểm tra trong AI (làm thủ công hằng tháng)
Hỏi từng câu trên ChatGPT, Gemini, Perplexity; ghi lại có nhắc Let's Do It Vietnam không và trích nguồn nào:
1. World Cleanup Day ở Việt Nam do ai tổ chức?
2. Tham gia dọn rác tình nguyện ở Hà Nội như thế nào?
3. Các tổ chức môi trường phi lợi nhuận ở Việt Nam?
4. Doanh nghiệp muốn tổ chức hoạt động CSR dọn rác bãi biển ở Việt Nam thì liên hệ ai?
5. Volunteer beach cleanup Vietnam / Nha Trang / Da Nang

Bảng theo dõi: `Ngày | Câu hỏi | Nền tảng | Có nhắc? | Nguồn được trích`.

## Bước 2 — Làm nội dung dễ trích dẫn
- Mỗi bài mở đầu bằng 1–2 câu trả lời thẳng: *"Ngày [ngày], [số người] nhân viên The Body Shop cùng Let's Do It Vietnam thu gom [số kg] kg rác tại biển Đồ Sơn, Hải Phòng."*
- Mỗi bài có ít nhất một số liệu (người, kg, địa điểm, ngày).
- Tiêu đề H2 dạng câu hỏi; danh sách và bảng thay cho đoạn văn dài.

## Bước 3 — Nội dung trang /faq/ (bản nháp)
- **Let's Do It Vietnam là gì?** Phong trào World Cleanup Day tại Việt Nam từ 2015, thuộc mạng lưới Let's Do It World tại 190+ quốc gia.
- **World Cleanup Day diễn ra khi nào?** Ngày 20/9 hằng năm; từ 2024 là Ngày Quốc tế chính thức của Liên Hợp Quốc.
- **Tôi tham gia dọn rác thế nào?** Tìm điểm gần bạn trên bản đồ `/cleanup-map/` rồi bấm "Register to Join", hoặc đăng ký tại `/join-us/`.
- **Tham gia có mất phí không?** [Xác nhận với ban tổ chức.]
- **Tôi có thể tự tổ chức một điểm dọn rác không?** Có, bạn có thể đăng ký làm người tổ chức (cleanup organiser).
- **Doanh nghiệp hợp tác thế nào?** Liên hệ letsdoitvietnam@gmail.com hoặc hotline 035.872.6755. Đối tác hiện có: VinUniversity, Hilton, The Body Shop, The Empyrean Cam Ranh, Unilever Vietnam…

## Bước 4 — llms.txt (đặt tại https://letsdoitvietnam.org/llms.txt)
Bản sẵn dùng: `outputs/llms.txt`.

## Bước 5 — Có mặt ở nơi AI hay đọc
- Wikipedia tiếng Việt và tiếng Anh: kiểm tra đã có trang "Let's Do It! Vietnam" chưa; nếu có thì bổ sung nguồn.
- Báo chí: mỗi sự kiện lớn có một thông cáo (`09-public-relations.md`). Bài báo là nguồn AI trích dẫn nhiều nhất.
- Trang của đối tác (VinUni, Hilton…) liên kết ngược về website.
