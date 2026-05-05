from datetime import datetime

print("\n--- CHUYỂN CHUỖI SANG DATETIME ---")
S = 'Sep 18 2019 2:43PM'
# Định dạng: %b (tháng viết tắt), %d (ngày), %Y (năm), %I (giờ 12h), %M (phút), %p (AM/PM)
dinh_dang = '%b %d %Y %I:%M%p'

dt_obj = datetime.strptime(S, dinh_dang)
print(f"Chuỗi ban đầu: {S}")
print(f"Kiểu dữ liệu sau khi chuyển: {type(dt_obj)}")
print(f"Giá trị datetime: {dt_obj}")