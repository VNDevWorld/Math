# Math Content Rules — Quy tắc biên soạn chung

Áp dụng cho dữ liệu Toán các lớp trong `allMath.json`. Đọc file này cùng file lộ trình của lớp đích trước khi làm việc.

## 1. Phạm vi và cách áp dụng

- File dữ liệu là `allMath.json`, giữ đúng chữ hoa/thường và schema hiện có.
- Chọn lớp bằng `classNo` theo yêu cầu; không mặc định lớp 5.
- Chỉ sửa lớp, đề và nội dung thuộc phạm vi được yêu cầu. Giữ nguyên dữ liệu khác.
- Tài liệu này quy định cách biên soạn; file `GRADE<N>_MATH_ROADMAP.md` quy định kiến thức, thứ tự học và giới hạn nội dung riêng của lớp N.
- Yêu cầu hiện tại của người dùng được ưu tiên hơn các quy tắc mặc định. Nêu rõ những thay đổi có ý nghĩa.
- Không tự di chuyển đề, đánh lại ID, xóa câu trùng hoặc thay dữ kiện khi chỉ được yêu cầu thêm câu.

## 2. Lộ trình riêng theo lớp

- Chỉ sử dụng file lộ trình đã tồn tại và phù hợp với lớp đích; không coi ví dụ tên file là một file đã có.
- Không sao chép lộ trình lớp 5 rồi chỉ đổi tên để dùng cho lớp 6, 7 hoặc lớp khác.
- Không áp giới hạn lớp 5, như tọa độ chỉ ở góc phần tư thứ nhất, cho lớp lớn hơn.
- Nếu chưa có lộ trình lớp đích, vẫn có thể nhập danh sách câu cụ thể theo yêu cầu và các quy tắc chung. Nêu rõ chưa có lộ trình riêng; không tuyên bố đã đối chiếu chuẩn chương trình.
- Khi được yêu cầu xây dựng lộ trình hoặc đánh giá độ phù hợp của nội dung, xác định chuẩn tham chiếu của lớp; đối chiếu chuẩn bang/trường nếu người dùng chỉ định.
- Không tự thêm kiến thức để lấp phần còn thiếu khi người dùng chỉ yêu cầu nhập danh sách câu.

## 3. Thêm đề và quản lý ID

1. Đọc cấu trúc thực tế của `allMath.json` trước khi sửa; không dựa hoàn toàn vào số đề trong lịch sử chat.
2. Mỗi đề mới mặc định **5 câu**, có 4 lựa chọn mỗi câu và đúng một đáp án đúng.
3. Giữ thứ tự câu người dùng gửi, kể cả câu lặp lại, trừ khi được yêu cầu loại trùng hoặc sắp xếp lại.
4. Với yêu cầu mỗi đề đúng 5 câu, nếu số câu không chia hết cho 5 thì hỏi cách xử lý phần dư; không tự bịa câu hoặc bỏ câu.
5. Nếu người dùng chỉ định rõ một đề có số câu khác 5, giữ đủ câu và thông báo.
6. Nếu không chỉ định ID mới, nối tiếp ID đề lớn nhất hiện tại của lớp đích.
7. Đề mới và câu mới dùng `status: 0` theo cấu trúc hiện có.
8. ID câu trong một đề bắt đầu từ 1 và tăng liên tục; ID đề không trùng nhau.
9. Khi chuyển vị trí đề, giữ thứ tự tương đối trong các nhóm; chỉ đánh lại ID đề khi người dùng yêu cầu. Giữ nguyên câu hỏi, đáp án, gợi ý, ID câu và trạng thái.
10. Không tự áp thứ tự chương trong file lộ trình của lớp để di chuyển các đề đã có. Chỉ sắp xếp lại ngân hàng khi người dùng yêu cầu.

## 4. Localization bắt buộc

Localize cả `question`, từng phần tử của `answers`, `correctAnswer` và `hint`.

| Field | Language |
| --- | --- |
| `enString` | English |
| `vnString` | Tiếng Việt |
| `koString` | 한국어 — Korean |
| `jaString` | 日本語 — Japanese |
| `cnTraditionalString` | 繁體中文 — Traditional Chinese |
| `arString` | العربية — Arabic |
| `frenchString` | Français — French |
| `germanString` | Deutsch — German |
| `italiaString` | Italiano — Italian |
| `portugueseBRString` | Português do Brasil — Brazilian Portuguese |
| `spanishString` | Español — Spanish |

- Không chép tiếng Anh vào các field khác để thay cho bản dịch.
- Giữ đúng tên field trong schema, kể cả `vnString` và `italiaString`; không tự đổi sang mã ngôn ngữ khác.
- Biểu thức số học, số, ký hiệu và tên riêng có thể giống nhau giữa các ngôn ngữ.
- Dịch rõ đơn vị, thương/số dư và các đại lượng trong đáp án có nhiều phần.
- Giữ cùng vị trí đáp án đúng trong cả 11 ngôn ngữ.
- Không thay đổi dữ kiện, đơn vị hoặc ý nghĩa phép tính khi dịch.

## 5. Quy tắc toán học và biên soạn lựa chọn

- Phân biệt **whole-number division with remainders** với **decimal quotients** theo nhóm bài. Không tự đổi câu chia có dư sang đáp án thập phân.
- Với phép chia số tự nhiên, số chia phải dương: dividend = divisor × quotient + remainder; 0 ≤ remainder < divisor. Không áp dụng máy móc quy ước này cho bài số âm ở lớp lớn hơn.
- Nếu câu hỏi yêu cầu cả quotient và remainder, ghi rõ số dư, kể cả khi bằng 0.
- Bài toán thực tế phải xử lý số dư theo ngữ cảnh: số nhóm đầy, phần dư, số xe cần làm tròn lên, hay ngày cần bổ sung vật tư.
- Câu hỏi nhiều đại lượng phải có đáp án nêu đủ và phân biệt rõ từng đại lượng.
- Dùng phép tính thập phân chính xác, như `Decimal`, cho so sánh và làm tròn; không dùng sai số float để quyết định đáp án.
- Với số dương, dùng quy tắc làm tròn phổ thông: chữ số xét từ 5 trở lên thì tăng; dưới 5 thì giữ. Không dùng mặc định kiểu làm tròn nửa về số chẵn của ngôn ngữ lập trình.
- Giữ số chữ số phù hợp khi làm tròn: ví dụ nearest tenth là `90.0`, nearest hundredth là `142.00`.
- Phân biệt `six hundred eight thousandths` = `0.608` và `six hundred and eight thousandths` = `600.008`.
- Lựa chọn sai phải khác nhau cả về giá trị lẫn ý nghĩa; không có hai cách viết cùng một đáp án đúng trong một câu.
- Câu so sánh có thể dùng `<`, `>`, `=` và một lựa chọn sai được dịch đúng ngôn ngữ, thay vì thêm ký hiệu tạo ra đáp án đúng thứ hai.
- Phân bố vị trí đáp án đúng; không đặt tất cả ở lựa chọn đầu tiên.
- Gợi ý nêu được cách tính hoặc lý do, không chỉ lặp đáp án.
- Nếu dữ kiện mâu thuẫn hoặc không xác định được đáp án duy nhất, nêu rõ vấn đề. Không tự đổi số liệu để tạo một đáp án đẹp. Có thể giữ nguyên và đưa đáp án dữ kiện không hợp lệ nếu phù hợp; nếu cần sửa dữ kiện, hỏi người dùng trước.

## 6. Kiểm tra trước khi hoàn tất

- JSON đọc được; schema của đề/câu và đủ 11 field ngôn ngữ phù hợp dữ liệu hiện có.
- Đúng số đề, số câu và thứ tự được yêu cầu; ID không trùng hoặc bị nhảy ngoài dự kiến.
- Mỗi câu có 4 lựa chọn khác nhau và đúng một đáp án đúng trong mọi ngôn ngữ.
- Kiểm tra lại phép tính, số dư, đơn vị, bài toán nhiều bước và các trường hợp làm tròn có nhớ.
- Nội dung tiếng Anh và bản dịch có cùng dữ kiện, cùng đáp án và cùng vị trí lựa chọn đúng.
- So sánh trước/sau để xác nhận không đổi dữ liệu ngoài phạm vi.
- Khi báo kết quả, ghi ngắn gọn: file đã sửa, dải ID, số câu, localization và mọi dữ kiện đã điều chỉnh hoặc còn bất thường.

## 7. Mẫu yêu cầu

> Đọc `MATH_CONTENT_RULES.md` và `GRADE5_MATH_ROADMAP.md`. Thêm các câu sau vào lớp 5 trong `allMath.json`, mỗi đề 5 câu, nối tiếp ID hiện tại và localize đủ 11 ngôn ngữ.

> Đọc `MATH_CONTENT_RULES.md`. Thêm các câu sau vào lớp 6 trong `allMath.json`, mỗi đề 5 câu, giữ thứ tự và localize đủ 11 ngôn ngữ. Nếu chưa có lộ trình lớp 6, chỉ nhập câu theo danh sách này.

> Đọc `MATH_CONTENT_RULES.md`. Xây dựng file `GRADE7_MATH_ROADMAP.md` theo chuẩn chương trình được chỉ định. Chưa sửa `allMath.json`.
