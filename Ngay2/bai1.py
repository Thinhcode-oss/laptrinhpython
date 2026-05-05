from datetime import datetime
import math

# Lấy thời gian hiện tại
now = datetime.now()

print("--- THÔNG TIN THỜI GIAN HIỆN TẠI ---")
print(f"Năm hiện tại: {now.year}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.strftime('%U')}")

# Tính tuần trong tháng: (ngày hiện tại // 7) + 1
week_of_month = math.ceil(now.day / 7)
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {week_of_month}")

print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {now.day}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")