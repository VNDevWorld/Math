# Kết quả kiểm tra Social Studies lớp 5

Ngày: 2026-11-12.

## Kết quả

- File: `data/alle12.json`.
- Block duy nhất thay đổi: `classNo=5`, `subject="socialStudies"`, `id=85`.
- Thêm 20 đề (ID 11–30), 100 câu (ID 51–150).
- Block sau bổ sung: 30 đề, 150 câu; tổng 60 block trong file không đổi.
- 100 câu mới có đủ 5 ngôn ngữ: 500 phiên bản câu hỏi, đầy đủ đáp án và lời giải.
- Giữ nguyên 10 đề/50 câu cũ trong block và toàn bộ 59 block còn lại.
- Kiểm tra hoàn nguyên phần chèn khôi phục chính xác mọi byte của file gốc.
- SHA256 trước: `f82b3646c053f27791a58724671e38a420020d7812e9e4e10d105389a5d96521`.
- SHA256 sau: `ef7ad2121417d206e0e11aa0c10dd581579f134e1d9c0d08a6b312ab3fc3fa7a`.

## Các kiểm tra đã đạt

- JSON đọc lại thành công; đúng key và kiểu dữ liệu.
- Mỗi đề 5 câu; mỗi câu 4 lựa chọn; `status=0` ở đề mới.
- ID duy nhất trong block; dãy ID cũ không thay đổi.
- LocalizedText đủ đúng 5 key; không chuỗi rỗng hoặc khoảng trắng thừa ở đầu/cuối.
- `correctAnswer` khớp nguyên object tại một vị trí duy nhất; mỗi ngôn ngữ cũng khớp duy nhất.
- Mỗi ngôn ngữ không có lựa chọn trùng sau chuẩn hóa.
- Phần dẫn của 100 câu mới không trùng sau chuẩn hóa với toàn bộ dữ liệu lớp 5 cũ hoặc trong đợt mới.
- Rà soát câu gần trùng: không có cặp phần dẫn tiếng Anh mới vượt ngưỡng tương đồng 0,80; không có câu mới với câu lớp 5 cũ vượt 0,78 (SequenceMatcher trên chuỗi đã chuẩn hóa).
- Các trường question và hint ngoài tiếng Anh không phải bản sao tiếng Anh; câu tiếng Ả Rập có chữ Ả Rập và không dùng ký tự ép đảo chiều.
- Bốn vị trí đáp án đúng xuất hiện 25 lần mỗi vị trí, cùng chỉ số đúng ở cả 5 ngôn ngữ.
- Ma trận: lịch sử 25, địa lý 20, công dân 20, kinh tế 20, văn hóa 15.
- Tư duy: nhận biết 30, hiểu 40, vận dụng 30.
- Độ khó: cơ bản 30, trung bình 50, thử thách 20.
- Localization: 60 câu chung, 40 câu bản địa hóa.
- Mỗi đề có 3 câu chung/2 câu bản địa hóa, ít nhất 3 chủ đề, 2 thao tác tư duy và một câu vận dụng.
- Không lặp cùng thứ tự 5 chủ đề giữa các đề.
- Câu hỏi tiếng Anh tối đa 30 từ, không cần ảnh/âm thanh ngoài dữ kiện văn bản.
- Đã rà soát nội dung và sửa các phương án nhiễu không phù hợp, đối chiếu đáp án với từng phiên bản và hint.

## Phạm vi localization

- enString: tiếng Anh/Hoa Kỳ.
- frenchString: tiếng Pháp/Pháp.
- idString: tiếng Indonesia/Indonesia.
- vnString: tiếng Việt/Việt Nam.
- arString: tiếng Ả Rập chuẩn hiện đại; bối cảnh chung và địa điểm cụ thể ghi rõ, không coi thế giới Ả Rập là một quốc gia.
- Các mốc/di tích thực được đối chiếu nguồn; cuộc họp, hồ sơ, khảo sát, ngân sách và tình huống giả định không được trình bày là sự kiện thực.

## Giới hạn kiểm chứng

- Bản dịch do mô hình biên soạn và rà soát ý nghĩa; chưa được người bản ngữ độc lập kiểm duyệt.
- Không tuyên bố bám sát chương trình lớp 5 chính thức của năm quốc gia/thị trường.
- Chưa tìm thấy tham chiếu trực tiếp tới `alle12.json` hay `idString` trong code Swift đã tìm trong `mathapps`.
- Model liên quan trong `toan5/Helper/OnlineDB/TestClassUnit.swift` yêu cầu `germanString` và không có `idString`; schema của alle12.json hiện tại không có germanString. Đây là giới hạn tích hợp có sẵn, không phải thay đổi schema trong đợt này.
- Code model liên quan cho thấy correctAnswer là LocalizedString, hiển thị hint theo ngôn ngữ và so sánh chuỗi đáp án. Code ở toancap1 có đảo cả object lựa chọn; chỉ class root có primary key trong các model TestClassUnit đã xem.
- Vì chưa xác nhận được consumer thực của file, không tuyên bố đã kiểm thử chạy app hoặc hiển thị RTL. Không sửa code ứng dụng hay thêm germanString.
- Một số trang UNESCO trả trang xác minh trình duyệt. Các nội dung tương ứng được kiểm tra qua bản lập chỉ mục, quyết định hoặc PDF chính thức; xem SOURCES.md.
- Các nguồn tiếng Anh/quốc tế hỗ trợ khái niệm chung; không dùng chúng để suy diễn quy định pháp luật riêng của quốc gia khác.

## Vấn đề dữ liệu cũ được giữ nguyên

- 50/50 câu Social Studies lớp 5 cũ có đáp án đúng ở vị trí đầu tiên.
- Các trường ngôn ngữ của 50 câu cũ đều đang sao chép tiếng Anh.
- Hint của dữ liệu cũ nhắc lại đáp án, thiếu giải thích.
- Câu ID 12 và 45 trùng phần dẫn về thủ đô Hoa Kỳ.
- Câu 19 và 36 gần trùng về văn kiện mở đầu bằng “We the People”; câu 14, 23 và 46 gần trùng về cơ quan làm luật.
- Một số câu cũ dùng cách hỏi nguyên nhân chính quá rộng (ví dụ ID 5 về người định cư); không sử dụng làm mẫu chất lượng.
- Các mục này chỉ được báo cáo, không tự sửa.

## Tài liệu kèm theo

- [MATRIX.md](MATRIX.md): ma trận 100 câu và 500 bối cảnh ngôn ngữ.
- [SOURCES.md](SOURCES.md): nguồn, phạm vi kiểm chứng và 500 dòng đối chiếu theo ngôn ngữ.
- [matrix.json](matrix.json): metadata bên ngoài schema ứng dụng.
