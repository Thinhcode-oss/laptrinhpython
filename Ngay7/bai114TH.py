import math

def so_than_thien():
    print("--- BAI 114: SO THAN THIEN ---")
    try:
        a = int(input("Nhap so nguyen a (>= 10): "))
        b = int(input("Nhap so nguyen b (<= 30000): "))
        
        if not (10 <= a <= b <= 30000):
            print("Vui long nhap a va b thoa man dieu kien: 10 <= a <= b <= 30000")
            return
            
    except ValueError:
        print("Loi: Vui long nhap so nguyen!")
        return

    danh_sach_kq = []
    
    # Du yet tu a den b
    for num in range(a, b + 1):
        # Dao nguoc so bang cach chuyen sang chuoi, dao chuoi [::-1], roi ep lai thanh so
        num_dao_nguoc = int(str(num)[::-1])
        
        # Kiem tra Uoc chung lon nhat co bang 1 hay khong
        if math.gcd(num, num_dao_nguoc) == 1:
            danh_sach_kq.append(num)
            
    # In ket qua
    print(f"\nCac so than thien trong khoang tu {a} den {b} la:")
    # In cac so cach nhau boi dau phay
    print(", ".join(map(str, danh_sach_kq))) 
    print(f"Tong cong co {len(danh_sach_kq)} so than thien duoc tim thay.")

# Chay thu bai 114
# so_than_thien()