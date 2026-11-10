# Grade 5 Math — Lộ trình học

Tài liệu này ghi lại các quyết định của dự án để sử dụng cho những yêu cầu sau.
Khi người dùng yêu cầu làm theo file này, đọc cả [MATH_CONTENT_RULES.md](MATH_CONTENT_RULES.md) và tài liệu này trước khi sửa dữ liệu.
Quy tắc JSON, chia đề, quản lý ID, localization và kiểm tra chung được lưu trong file quy tắc chung; tài liệu này giữ phần riêng của lớp 5.
Nếu yêu cầu mới của người dùng khác tài liệu, ưu tiên yêu cầu mới và nêu rõ điểm thay đổi.

## 1. Phạm vi

- File dữ liệu: `allMath.json` (đúng chữ hoa/thường).
- Chỉ sửa đối tượng có `classNo: 5`, trừ khi người dùng chỉ định lớp khác.
- Dùng Common Core Grade 5 làm mốc; đây không phải chương trình bắt buộc chung cho mọi bang ở Mỹ.
- Mục tiêu: hiểu khái niệm, làm được phép tính, giải thích cách làm và vận dụng vào bài toán có lời văn.
- Không thay đổi các lớp khác hoặc sửa các đề cũ ngoài phạm vi được yêu cầu.
- File này hướng dẫn công việc; việc tạo file không đồng nghĩa với việc đã sắp xếp lại ngân hàng câu hỏi.

## 2. Thứ tự học chính đã thống nhất

Giữ tên chương và tên kỹ năng bằng tiếng Anh. Toàn bộ Decimals nằm trong **một chương**, gồm các nhóm kỹ năng bên dưới; không tách thành nhiều chương ngang hàng.

| Order | Chapter | Learning sequence |
| --- | --- | --- |
| 1 | Whole-Number Multiplication | Multiply Multi-digit by 1-digit → Multiply 2-digit by 2-digit → Multiply 3-digit by 2-digit → Multiplication Word Problems → Multi-step Word Problems |
| 2 | Whole-Number Division | Division Facts → Divide by Multiples of 10 → Divide 2-, 3-, and 4-digit Numbers by 1-digit Divisors → Divide by 2-digit Divisors → Division Word Problems |
| 3 | Decimals | Decimal Place Value → Rounding Decimals → Powers of Ten → Adding and Subtracting Decimals → Multiplying Decimals → Dividing Decimals → Decimal Word Problems |
| 4 | Fraction Foundations | Equivalent Fractions → Simplify Fractions → Fractions as Division → Improper Fractions and Mixed Numbers → Fractions and Mixed Numbers to Decimals |
| 5 | Fraction Addition and Subtraction | Like Denominators → Unlike Denominators → Subtract Fraction from Whole Number → Fraction Word Problems |
| 6 | Mixed-Number Addition and Subtraction | Addition → Subtraction without Regrouping → Subtraction with Regrouping → Mixed-Number Word Problems |
| 7 | Fraction Multiplication and Applications | Fraction of a Set → Fractions × Whole Numbers → Fractions × Fractions with Area Models → Simplifying Products → Mixed Numbers → Word Problems |
| 8 | Numerical Expressions | Order of Operations with +, −, ×, ÷ and Grouping Symbols → Write and Interpret Numerical Expressions → Numerical Patterns |
| 9 | Two-Dimensional Geometry | Classify Triangles → Classify Quadrilaterals → Relationships Between Shape Categories → Rectangles and Composite Rectangles |
| 10 | Volume | Unit Cubes → Volume of Rectangular Prisms → Volume of Composite Rectangular Prisms → Volume Word Problems |
| 11 | Coordinate Geometry | Coordinate Axes and Origin → Plot Ordered Pairs → Interpret Coordinates → Graph Numerical Patterns |

Các bài nền tảng từ lớp trước chỉ dùng để ôn hoặc làm cầu nối. Không coi tất cả các bài ôn là nội dung mới bắt buộc của lớp 5.

### Chi tiết chương Decimals

1. **Decimal Place Value**: đọc, viết bằng chữ và chữ số; dạng khai triển; so sánh và sắp xếp.
2. **Rounding Decimals**: nearest whole number → nearest tenth → nearest hundredth → mixed place values.
3. **Powers of Ten**: quan hệ giữa các hàng; nhân/chia với 10, 100, 1,000; cách viết 10², 10³.
4. **Adding and Subtracting Decimals**.
5. **Multiplying Decimals**: by Whole Numbers → by Decimals.
6. **Dividing Decimals**: Whole Numbers to Decimal Quotients → Decimals by Whole Numbers → Decimals by Decimals; kết quả chính xác trước, làm tròn thương sau.
7. **Decimal Word Problems**: một bước → nhiều bước → mixed operations.

Đọc, viết, so sánh đến hàng phần nghìn. Phần bốn phép tính cốt lõi tập trung số thập phân đến hàng phần trăm; giải thích bằng giá trị hàng và mô hình, không chỉ thuộc quy tắc.

## 3. Các phần cần bổ sung khi hoàn thiện toàn bộ chương trình

Danh sách kỹ năng gốc chưa bao phủ đủ các nội dung sau:

- **Unit Fraction Division**: học sau phần nhân phân số; chia phân số đơn vị cho số tự nhiên và số tự nhiên cho phân số đơn vị, ví dụ 1/3 ÷ 4 và 4 ÷ 1/3. Không mở rộng mặc định sang chia hai phân số bất kỳ.
- **Multiplication as Scaling** và **Area of Rectangles with Fractional Side Lengths**: tích hợp vào chương phân số.
- **Measurement Conversions**: đổi đơn vị trong cùng hệ đo, kết hợp bài toán nhiều bước; học sau khi có nền tảng phép tính cần thiết.
- **Fractional Line Plots**: biểu đồ chấm trên trục số với số đo 1/2, 1/4, 1/8; học sau cộng, trừ phân số. Phân biệt với **Line Graphs**.
- **Numerical Patterns** và **Write and Interpret Numerical Expressions**: tích hợp vào Numerical Expressions rồi nối với Coordinate Geometry.

Khi người dùng chỉ yêu cầu nhập một danh sách câu hỏi, không tự sinh thêm các câu thuộc những phần thiếu này. Khi người dùng yêu cầu hoàn thiện chương trình, đưa chúng vào kế hoạch biên soạn.

## 4. Giới hạn nội dung

- Coordinate Geometry cốt lõi dùng **first quadrant**; không mặc định thêm tọa độ âm, slope hay phương trình đường thẳng.
- Volume cốt lõi dùng hình hộp chữ nhật có cạnh là số tự nhiên và các khối ghép phù hợp.
- Giữ Powers of Ten trong lớp 5; không mặc định thêm thứ tự phép tính có số mũ tổng quát.
- Không đưa vào lộ trình cốt lõi: diện tích tam giác/hình bình hành/đa giác tổng quát; surface area; mean/median/mode/range như một chương thống kê; quan hệ góc đối đỉnh, phụ nhau, bù nhau ở mức bài toán nâng cao.
- Tally Charts, Picture Graphs, Bar Graphs và các bài cơ bản đã học chỉ là ôn tập nếu cần.
- Khi người dùng chủ động cung cấp câu ngoài phạm vi, không âm thầm bỏ: giải thích ngắn và xử lý theo yêu cầu cụ thể của họ.

## 5. Mốc sắp xếp đã thực hiện

Sau khi tạo đủ 149 đề, người dùng yêu cầu đưa đề cũ 1–19 xuống cuối:

- Đề cũ 20–149 trở thành đề 1–130.
- Đề cũ 1–19 trở thành đề 131–149.

Đây là mốc lịch sử, **không phải thao tác cần chạy lại**. Những lần sau luôn đọc ID hiện tại từ file.

## 6. Mẫu yêu cầu sử dụng lại

> Đọc `MATH_CONTENT_RULES.md` và `GRADE5_MATH_ROADMAP.md` trong thư mục dữ liệu và làm theo. Thêm các câu dưới đây vào lớp 5 trong `allMath.json`, mỗi đề 5 câu, nối tiếp ID hiện tại, giữ thứ tự câu và localize đủ 11 ngôn ngữ.

> Đọc `MATH_CONTENT_RULES.md` và `GRADE5_MATH_ROADMAP.md`. Kiểm tra ngân hàng đề lớp 5 đang có so với lộ trình; liệt kê phần còn thiếu trước, chưa sửa dữ liệu.

> Đọc `MATH_CONTENT_RULES.md` và `GRADE5_MATH_ROADMAP.md`. Lập bảng ánh xạ từ ID đề hiện tại sang các chương trong lộ trình để tôi xem; chưa chuyển vị trí hoặc đánh lại ID.

## 7. Nguồn tham chiếu

- [Grade 5 overview](https://www.thecorestandards.org/Math/Content/5/introduction/)
- [Number & Operations in Base Ten](https://www.thecorestandards.org/Math/Content/5/NBT/)
- [Fractions](https://www.thecorestandards.org/Math/Content/5/NF/)
- [Operations & Algebraic Thinking](https://www.thecorestandards.org/Math/Content/5/OA/)
- [Measurement & Data](https://www.thecorestandards.org/Math/Content/5/MD/)
- [Geometry](https://www.thecorestandards.org/Math/Content/5/G/)

Khi được yêu cầu đối chiếu với một bang, trường hoặc chương trình cụ thể, kiểm tra chuẩn của nơi đó thay vì coi Common Core là chuẩn duy nhất.
