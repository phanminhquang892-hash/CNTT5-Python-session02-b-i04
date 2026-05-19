""" 
Input
| Thông tin       | Dữ liệu nhập ban đầu |
| --------------- | -------------------- |
| Mã bệnh nhân    | str                  |
| Nhiệt độ cơ thể | str                  |
| Nhịp tim        | str                  |

Output mong muốn
| Thông tin       | Kiểu dữ liệu cần lưu |
| --------------- | -------------------- |
| Mã bệnh nhân    | str                  |
| Nhiệt độ cơ thể | float                |
| Nhịp tim        | int                  |

Giải pháp 1: Ép kiểu trực tiếp khi nhập
temperature = float(input("Nhập nhiệt độ: "))

Giải pháp 2: Nhập chuỗi trước rồi ép kiểu sau
temperature_input = input("Nhập nhiệt độ: ")
temperature = float(temperature_input)

Chọn: Giải pháp 2
Lý do:
Dữ liệu của bệnh nhân trong bệnh viện:

Dữ liệu cần đc kiểm tra kỹ
Dễ dò lỗi khi nhập sai
Có thể kiểm tra dữ liệu trước khi ép kiểu

"""
patient_code = input("Nhập mã bệnh nhân: ")
temperature_1 = input("Nhập Nhiệt độ cơ thể: ")
heart_rate_1 = input("Nhập nhịp tim: ")

# ép kiểu
temperature = float(temperature_1)
heart_rate = int(heart_rate_1)

print(f" Mã bệnh nhân: {patient_code}"
      f" Nhiệt độ cơ thể: {temperature}"
      f" Nhịp tim: {heart_rate}") 