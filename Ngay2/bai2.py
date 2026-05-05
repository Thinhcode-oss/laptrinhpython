from datetime import date

print("\n--- TÍNH KHOẢNG CÁCH GIỮA 2 NGÀY ---")
# Nhập ngày thứ nhất
d1 = int(input("Nhập ngày 1: "))
m1 = int(input("Nhập tháng 1: "))
y1 = int(input("Nhập năm 1: "))

# Nhập ngày thứ hai
d2 = int(input("Nhập ngày 2: "))
m2 = int(input("Nhập tháng 2: "))
y2 = int(input("Nhập năm 2: "))

date1 = date(y1, m1, d1)
date2 = date(y2, m2, d2)

delta = abs((date2 - date1).days)
print(f"Số ngày cách nhau giữa 2 ngày là: {delta} ngày")