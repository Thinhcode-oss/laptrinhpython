def tinh_tien_thoi(so_tien):
    """
    Ham tinh toan va in ra cac loai tien can doi sao cho so luong to la it nhat
    Chi in ra cac loai tien co so luong > 0
    """
    # Danh sach 9 loai menh gia tien sap xep tu lon den be
    cac_loai_tien = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    tong_so_to = 0
    tong_so_loai = 0
    
    print(f"So tien {so_tien} duoc doi thanh")
    
    for menh_gia in cac_loai_tien:
        # Tinh so luong to cua menh gia hien tai
        so_luong = so_tien // menh_gia 
        
        # Chi xu ly va in ra neu so luong > 0
        if so_luong > 0:
            print(f"  Loai {menh_gia} gom {so_luong} to")
            tong_so_to += so_luong
            tong_so_loai += 1
            
            # Cap nhat lai so tien con lai can doi
            so_tien = so_tien % menh_gia
            
    print(f"TONG CONG CO {tong_so_to} TO")
    print(f"Tong so loai = {tong_so_loai}")

def phan_mem_thu_ngan():
    """
    Ham mo phong chuong trinh thu ngan theo yeu cau phan Mo rong
    """
    print("--- CHUONG TRINH THU NGAN ---")
    try:
        a = int(input("Nhap so tien hang can phai tra (a) "))
        b = int(input("Nhap so tien khach hang thuc te tra (b) "))
    except ValueError:
        print("Loi Vui long nhap so nguyen hop le")
        return

    print("-" * 30)
    
    if a > b:
        print(f"Thong bao So tien khach hang con thieu la {a - b}")
        print("Ket thuc chuong trinh")
    elif a == b:
        print("Cam on khach hang Hen gap lai")
    else: # a < b
        tien_thoi_lai = b - a
        print("Goi y thoi tien cho khach")
        
        # Goi ham tinh tien thoi o tren
        tinh_tien_thoi(tien_thoi_lai)
        
        # Cho nguoi dung nhan Enter de ket thuc
        input("\n[Nhan phim Enter de hoan tat giao dich]")
        print("Cam on khach hang Hen gap lai")

# Chạy chương trình
if __name__ == "__main__":
    phan_mem_thu_ngan()