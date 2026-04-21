# Nhập dữ liệu từ bàn phím
chieu_dai = float(input("Nhập chiều dài đáy hình chữ nhật (cm) :>? "))
chieu_rong = float(input("Nhập chiều rộng đáy hình chữ nhật (cm) :>? "))
chieu_cao = float(input("Nhập chiều cao hình khối chữ nhật (cm) :>? "))
so_le = int(input("Số lượng số lẻ cần hiển thị :>? "))

# Tính toán
dien_tich_day = chieu_dai * chieu_rong
the_tich = dien_tich_day * chieu_cao

# Xuất kết quả với định dạng số lẻ động
# Sử dụng f-string với định dạng .nf trong đó n là số_le
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f}cm^2")
print(f"Thể tích hình khối = {the_tich:.{so_le}f}cm^3")