""" 
Giải pháp 1: Gộp điều kiện (Flat Logic)
if age < 75 and 90 <= blood_pressure <= 140 and blood_sugar < 150:
 - Ưu điểm
Ngắn gọn
Dễ viết
Ít dòng code
 - Nhược điểm
Khó biết bệnh nhân trượt điều kiện nào
Thông báo lỗi chưa chi tiết

Giải pháp 2: Điều kiện lồng nhau (Nested If)
if age < 75:
    if 90 <= blood_pressure <= 140:
        if blood_sugar < 150:
 - Ưu điểm
Dễ thông báo lỗi cụ thể
Giá trị y khoa cao hơn
Dễ kiểm tra từng điều kiện
 - Nhược điểm
Code dài hơn
Nhiều thụt lề hơn

- Em chọn Nested If vì:
Có thể kiểm tra từng điều kiện rõ ràng
Dễ thông báo nguyên nhân bị từ chối
Phù hợp hệ thống y khoa cần độ an toàn cao

"""

age = int(input("Nhập tuổi bệnh nhân: "))
blood_pressure = int(input("Nhập huyết áp bệnh nhân: "))
blood_sugar = int(input("Nhập đường huyết bệnh nhân: "))

if age < 0 or blood_pressure < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ")
    exit()
    
if age > 75 :
    print("Từ chối phẫu thuật: Bệnh nhân vượt ngưỡng tuổi cho phép")
elif blood_pressure < 90 or blood_pressure > 140:
    print("Từ chối phẫu thuật: Huyết áp không an toàn")
elif blood_sugar >= 150:
    print("Từ chối phẫu thuật: Đường huyết quá cao")
else:
    print(" Đủ điều kiện để phẫu thuật")
