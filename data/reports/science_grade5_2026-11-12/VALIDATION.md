# Báo cáo bổ sung 10 đề Science lớp 5

Ngày: 2026-11-12.

## Kết quả

- File: `data/alle12.json`.
- Chỉ thêm vào block `classNo=5`, `subject="science"`, `id=65`.
- 10 đề mới: ID 11–20; 50 câu mới: ID 51–100.
- Block hiện có 20 đề / 100 câu. Tổng 60 block không đổi.
- Đủ 5 ngôn ngữ cho mỗi câu: 250 phiên bản, đầy đủ lựa chọn, đáp án và hint.
- Mỗi đề mới đúng 5 câu; mỗi câu 4 lựa chọn; `status=0`.
- SHA256 trước: `ef7ad2121417d206e0e11aa0c10dd581579f134e1d9c0d08a6b312ab3fc3fa7a`.
- SHA256 sau: `3df7293ee5d6e5885ac364ef6cdb07e670710a8142de1417afe1e58e1ba6b6e2`.

## Bảo toàn dữ liệu

- 10 đề Science cũ và 59 block khác được đối chiếu bằng dữ liệu JSON và giữ nguyên.
- Đối chiếu riêng block Social Studies lớp 5 id=85: giữ nguyên đầy đủ, gồm 20 đề được thêm trước đó.
- Bỏ đúng phần chèn khôi phục nguyên vẹn từng byte của file trước khi thực hiện.
- Trước khi ghi đã kiểm tra file hiện tại vẫn trùng bản đọc ban đầu.
- Sau ghi đã đọc lại JSON và đối chiếu toàn bộ với bản ứng viên.
- Không sửa code ứng dụng, không cài thư viện và không thêm field vào JSON.

## Ma trận và phân bố

- Sinh vật và hệ sinh thái: 15.
- Vật chất và sự biến đổi: 10.
- Lực, chuyển động và năng lượng: 10.
- Trái Đất, nước, thời tiết và không gian: 10.
- Thực hành khoa học: 5.
- Tư duy: nhận biết 15, giải thích/so sánh 20, vận dụng/suy luận 15.
- Độ khó: cơ bản 15, trung bình 25, thử thách 10.
- Mỗi đề có ít nhất 3 chủ đề, đủ ba thao tác tư duy, ít nhất một câu vận dụng và đúng một câu thử thách.
- Không lặp cùng thứ tự 5 chủ đề giữa các đề.
- Vị trí đáp án đúng: 13 / 13 / 12 / 12, cùng chỉ số ở cả năm ngôn ngữ; không có chuỗi bốn đáp án đúng liên tiếp ở cùng vị trí.
- Không áp dụng tỷ lệ bản địa hóa 30/20 hay cơ cấu 3/2, theo điều chỉnh cuối trong yêu cầu đính kèm. Kiến thức khoa học và dữ kiện được giữ tương đương giữa các bản dịch.

## Kiểm tra đã đạt

- JSON hợp lệ, đúng bộ key và kiểu dữ liệu ở mọi cấp mới.
- ID đề và ID câu duy nhất trong block; không đánh lại ID cũ.
- Mỗi LocalizedText đủ đúng 5 key, chuỗi không rỗng, không dư khoảng trắng đầu/cuối.
- correctAnswer khớp nguyên object tại đúng một vị trí trong answers.
- Mỗi ngôn ngữ có đúng một lựa chọn khớp chuỗi đáp án; không có lựa chọn trùng sau chuẩn hóa.
- Phần dẫn mới không trùng sau chuẩn hóa với dữ liệu lớp 5 cũ hoặc trong đợt mới, kiểm tra riêng cả năm ngôn ngữ.
- Tương đồng phần dẫn tiếng Anh tối đa với câu lớp 5 cũ: 0.650; tối đa giữa câu mới: 0.610, dùng SequenceMatcher sau chuẩn hóa. Đây chỉ là công cụ hỗ trợ, không chứng minh độc lập tính khác biệt về ý nghĩa.
- Đã rà soát nội dung để phân biệt ôn khái niệm bằng thao tác mới với diễn đạt lại câu cũ.
- question và hint ngoài tiếng Anh không phải bản sao tiếng Anh; tiếng Ả Rập có chữ đúng hệ và không chèn ký tự ép đảo chiều.
- Số câu đủ toàn bộ thành phần theo từng field: {'enString': 50, 'frenchString': 50, 'idString': 50, 'vnString': 50, 'arString': 50}.
- Câu hỏi tiếng Anh tối đa 39 từ; không cần ảnh hoặc âm thanh ngoài câu.
- Đã rà soát ý nghĩa từng phiên bản, sự nhất quán đơn vị/số liệu, hint và vị trí đáp án. Đã sửa các phương án nhiễu không phù hợp.
- Tình huống/số liệu tự biên soạn được nhận diện là giả định. Không gán dữ liệu giả định cho nghiên cứu thật.
- Nêu đủ đường dẫn mạch điện, điều kiện so sánh truyền nhiệt và hình học mô hình bóng đổ cần thiết.
- Hint giải thích khái niệm hoặc suy luận, không dùng A/B/C/D hay số thứ tự lựa chọn.

## Nguồn và giới hạn

- SOURCES.md có danh mục nguồn và 250 dòng đối chiếu theo ID/ngôn ngữ, phân biệt cơ sở khoa học với dữ kiện giả định.
- Nguồn được đối chiếu bằng công cụ web; một số thông tin dựa trên đoạn văn bản đã lập chỉ mục, không tuyên bố đã đọc toàn văn mọi PDF.
- Bản dịch do mô hình biên soạn và rà soát; chưa có người bản ngữ độc lập kiểm duyệt.
- Không tuyên bố bám sát chương trình chính thức của một quốc gia hoặc sách cụ thể.
- Báo cáo trước đã ghi nhận chưa xác định consumer trực tiếp của alle12.json. Model Swift liên quan ở toan5 yêu cầu germanString và không có idString; lần này đã đọc lại model và giữ nguyên schema của file theo yêu cầu.
- Code liên quan so sánh đáp án bằng chuỗi theo ngôn ngữ và hiển thị hint theo ngôn ngữ; code toancap1 có đảo nguyên object lựa chọn. Không xác nhận đây là consumer trực tiếp của alle12.json.
- Chưa kiểm thử chạy app hoặc giao diện tiếng Ả Rập/RTL. Không sửa code để xử lý giới hạn tích hợp có sẵn.

## Dữ liệu cũ: chỉ báo cáo, không sửa

- 50/50 câu Science lớp 5 cũ có đáp án đúng ở vị trí đầu tiên.
- Toàn bộ 350 object LocalizedText của 50 câu cũ đang lặp cùng chuỗi tiếng Anh cho cả 5 field.
- 50/50 hint cũ bằng correctAnswer, không có giải thích riêng.
- ID 43 diễn đạt tiêu hóa như quá trình phân giải thức ăn để lấy năng lượng; cần rà lại để phân biệt tiêu hóa với quá trình giải phóng năng lượng trong tế bào.
- ID 23 dùng đáp án “Condensed water vapor” cho mây; nên diễn đạt rõ các giọt nước nhỏ hoặc tinh thể băng thay vì gây nhầm mây là hơi nước vô hình.
- Những mục này không được chỉnh sửa trong đợt bổ sung.

## Tài liệu

- [MATRIX.md](MATRIX.md): ma trận, mục tiêu và điều kiện của từng ngôn ngữ.
- [SOURCES.md](SOURCES.md): bảng nguồn kiểm chứng.
- [matrix.json](matrix.json): metadata ngoài schema ứng dụng.
