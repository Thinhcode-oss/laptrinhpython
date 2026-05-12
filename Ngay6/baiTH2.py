import sys

def giai_quyet_doi_tien(X):
    # Danh sach menh gia tien
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    total_bills = 0
    total_types = 0
    
    print(f"\nSo tien {X} duoc doi thanh:")
    
    for coin in denominations:
        # Su dung toan tu chia lay nguyen // de tinh so to [cite: 7, 8]
        count = X // coin
        # Su dung toan tu chia lay du % de tinh so tien con lai [cite: 8, 9]
        X = X % coin
        
        # Chi in nhung loai tien co so to lon hon 0 theo yeu cau bai 20
        if count > 0:
            print(f"Loai {coin} gom {count} to")
            total_bills += count
            total_types += 1
            
    print(f"TONG CONG CO {total_bills} TO")
    print(f"Tong so loai = {total_types}")

# --- PHAN MO RONG ---
try:
    print("--- HE THONG THANH TOAN ---")
    a = int(input("Nhap so tien hang can tra (a): "))
    b = int(input("Nhap so tien khach dua (b): "))

    if a > b:
        print(f"So tien khach hang con thieu la: {a - b}")
    elif a == b:
        print("Cam on khach hang. Hen gap lai")
    else:
        # Truong hop a < b: Can thoi tien thua
        tien_thua = b - a
        giai_quyet_doi_tien(tien_thua)
        
        # Doi nguoi dung nhan Enter
        input("\nNhan phim Enter de tiep tuc...")
        print("Cam on khach hang. Hen gap lai")

except ValueError:
    print("Loi: Vui long nhap so nguyen hop le!")