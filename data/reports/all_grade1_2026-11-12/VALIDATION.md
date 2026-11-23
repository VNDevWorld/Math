# Báo cáo bổ sung đề tổng hợp lớp 1

Ngày: 2026-11-12.

## Kết quả

- File: `data/alle12.json`.
- Chỉ thêm vào `classNo=1`, `subject="all"`, `id=1`.
- 10 đề mới ID 21–30; 50 câu mới ID 101–150.
- Block sau bổ sung: 30 đề / 150 câu. Tổng số block trong file vẫn là 60.
- 250 phiên bản ngôn ngữ, đủ câu hỏi, bốn lựa chọn, đáp án và hint.
- SHA256 trước: `3df7293ee5d6e5885ac364ef6cdb07e670710a8142de1417afe1e58e1ba6b6e2`.
- SHA256 sau: `d3f90093fa3aa656d2117ddee865e58115a455490e50208c5e8524b29ea3f79c`.

## Bảo toàn dữ liệu

- 20 đề lớp 1 all cũ giữ nguyên dữ liệu và ID.
- Toàn bộ 59 block khác giữ nguyên, bao gồm block Science lớp 5 id=65 và Social Studies lớp 5 id=85 cùng các phần bổ sung trước đó.
- Bỏ chính xác phần chèn khôi phục nguyên vẹn từng byte của file trước khi thực hiện.
- Trước khi ghi đã kiểm tra file không thay đổi so với bản đọc ban đầu.
- Sau ghi đã đọc lại, parse JSON và đối chiếu toàn bộ với bản ứng viên.
- Không sửa code ứng dụng, không cài thư viện, không thêm field vào JSON và không sửa báo cáo cũ.

## Ma trận đã đạt

- Mỗi đề: 2 Toán, 1 Ngôn ngữ, 1 Khoa học, 1 Đời sống xã hội.
- Tổng: 20 Toán / 10 Ngôn ngữ / 10 Khoa học / 10 Đời sống xã hội.
- Toán: 5 đếm/thứ tự/so sánh số; 8 cộng/trừ; 4 hình/quy luật; 3 đo lường/so sánh có dữ kiện.
- Ngôn ngữ: 4 nghĩa/phân loại từ; 4 hiểu câu; 2 hiểu đoạn rất ngắn.
- Khoa học: 3 cơ thể/giác quan; 4 sinh vật/môi trường sống; 3 vật liệu/nước/hiện tượng.
- Đời sống: 4 hợp tác/ứng xử; 3 chăm sóc/giữ đồ chung; 3 nghề nghiệp/dịch vụ.
- Tư duy: 20 nhận biết / 20 hiểu-so sánh / 10 vận dụng.
- Độ khó: 25 cơ bản / 20 trung bình / 5 thử thách.
- Mỗi đề có ít nhất 2 thao tác tư duy, đúng một câu vận dụng và không quá một câu thử thách.
- Mười đề có mười thứ tự môn khác nhau.
- Vị trí đáp án đúng: 13 / 13 / 12 / 12; chỉ số đúng đồng bộ cả năm ngôn ngữ.

## Kiểm tra cấu trúc và nội dung

- JSON hợp lệ, đúng key và kiểu dữ liệu; mỗi đề 5 câu, mỗi câu 4 lựa chọn, status=0.
- ID đề và ID câu duy nhất trong block; không đánh lại ID cũ.
- Mỗi LocalizedText đủ đúng 5 key, không chuỗi rỗng hoặc dư khoảng trắng đầu/cuối.
- correctAnswer khớp chính xác một object trong answers; chuỗi từng ngôn ngữ cũng khớp duy nhất.
- Không lựa chọn trùng sau chuẩn hóa; ký hiệu toán +, −, =, < được giữ nghĩa khi kiểm tra, không bị coi là chuỗi rỗng.
- 18 kiểm tra bằng code cho số học, số thứ tự, đếm, dãy số, sắp xếp, quy luật và dữ kiện so sánh; hai câu hình học đối chiếu thuộc tính hình.
- Các bài toán chỉ dùng số trong phạm vi 20, kết quả không âm, không nhân/chia/phân số và không yêu cầu nhiều bước tính.
- So sánh khối lượng dùng các khối giống hệt nhau; sức chứa dùng cùng một thìa đầy cho cả hai cốc; độ dài cho số đo cùng đơn vị.
- Số câu đủ toàn bộ thành phần theo field: {'enString': 50, 'frenchString': 50, 'idString': 50, 'vnString': 50, 'arString': 50}.
- Không có question/hint ở field khác sao chép tiếng Anh; số, ký hiệu và tên riêng có thể trùng hợp lệ.
- Tiếng Ả Rập có đúng hệ chữ, không thêm ký tự ép đảo chiều và không có bài đọc phụ thuộc trái/phải của chuỗi.
- Câu hỏi mới không trùng sau chuẩn hóa với toàn bộ câu lớp 1 cũ hoặc trong đợt mới, kiểm tra riêng từng ngôn ngữ.
- Năm cờ tương đồng phần dẫn tiếng Anh được xem xét trong near_duplicate_review.json: bốn cờ là dạng hỏi từ vựng ngắn chung nhưng khác mục tiêu từ/nghĩa; một cờ là hai vị trí số thiếu khác nhau trong phép cộng và trừ. Giữ lại sau rà soát nội dung, không chỉ dựa vào điểm số.
- Các câu ôn giác quan/hợp tác/nghiệp vụ được đặt trong nhiệm vụ hoặc tình huống khác với câu định nghĩa cũ; không chỉ dịch lại câu cũ.
- Đã rà soát từng phiên bản về ý nghĩa, dữ kiện, phương án nhiễu và hint. Mỗi câu có một đáp án theo điều kiện/mục tiêu đã nêu.
- Câu hỏi tiếng Anh dài tối đa 19 từ; hint tiếng Anh tối đa 13 từ; hai đoạn đọc kèm câu hỏi lần lượt 11 và 13 từ tiếng Anh.
- Không cần ảnh/âm thanh; không emoji đếm vật; không câu về vần/chữ đầu tiếng Anh áp sang ngôn ngữ khác.
- Không dùng lựa chọn All of the above hoặc None of the above.
- Nội dung tự biên soạn là hư cấu; không thêm lời dẫn dài gây khó đọc cho trẻ và không gán dữ liệu hư cấu cho nguồn thực.

## Giới hạn

- Bản dịch do mô hình biên soạn và rà soát, chưa có người bản ngữ độc lập kiểm duyệt.
- Nhãn độ khó là đánh giá biên soạn; không tuyên bố bám chuẩn chương trình lớp 1 chính thức của từng quốc gia.
- Nguồn được tra qua công cụ web; một số đối chiếu dựa trên đoạn văn bản lập chỉ mục. Bảng kiểm chứng phân biệt nguồn kiến thức, code tính toán, chi tiết đoạn đọc và điều kiện tình huống.
- Giới hạn tích hợp đã có từ trước: chưa xác định consumer trực tiếp của alle12.json. Model Swift liên quan yêu cầu germanString và không có idString; giữ nguyên schema của file theo yêu cầu.
- Đã đọc lại model liên quan: đáp án/hint là LocalizedString; code toancap1 đảo nguyên object lựa chọn. Không xác nhận đây là consumer trực tiếp của file.
- Chưa chạy app hoặc kiểm thử giao diện RTL. Không thay đổi code để giải quyết giới hạn tích hợp có sẵn.

## Vấn đề cũ giữ nguyên

- 100/100 hint của block all lớp 1 cũ bằng đáp án, thiếu giải thích riêng.
- 700/700 object LocalizedText cũ lặp cùng chuỗi tiếng Anh ở năm field.
- Vị trí đúng ở 100 câu cũ: đầu 15, thứ hai 45, thứ ba 35, cuối 5.
- Câu 39 so sánh khối lượng đá/lông/giấy/lá mà thiếu kích thước hoặc số đo cụ thể.
- Câu 50 hỏi phương tiện nhanh nhất mà không giới hạn điều kiện hành trình.
- Câu 68 hỏi con vật biết bơi với dog/bird/elephant/lion; nhiều lựa chọn có thể phù hợp.
- Câu 83 hỏi giác quan nghe nhưng đáp án là cơ quan Ears; nên phân biệt hearing và ears.
- Các nội dung trên chỉ được báo cáo, không chỉnh sửa.

## Tài liệu

- [MATRIX.md](MATRIX.md): ma trận, mục tiêu và 250 phiên bản câu hỏi.
- [VERIFICATION.md](VERIFICATION.md): 250 dòng kiểm chứng theo ID và ngôn ngữ, kèm URL khi cần.
- [matrix.json](matrix.json): metadata bên ngoài schema ứng dụng.
- [math_checks.json](math_checks.json): kết quả kiểm tra số học/quy luật/dữ kiện.
- [near_duplicate_review.json](near_duplicate_review.json): ghi nhận rà soát tương đồng phần dẫn.
