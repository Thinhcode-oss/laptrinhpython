import math

# ==========================================
# BIỂU DIỄN TRI THỨC TOÁN TAM GIÁC LỚP 5
# ==========================================
class TamGiacLop5:
    """
    Biểu diễn tri thức tam giác lớp 5: Tập trung vào tính toán Chu vi và Diện tích.
    Các Fact (Sự kiện): Cạnh a, b, c; Cạnh đáy; Chiều cao; Chu vi; Diện tích.
    Các Rule (Luật): Công thức tính toán.
    """
    def __init__(self, a=None, b=None, c=None, canh_day=None, chieu_cao=None, chu_vi=None, dien_tich=None):
        # Các thuộc tính (Facts)
        self.a = a
        self.b = b
        self.c = c
        self.canh_day = canh_day
        self.chieu_cao = chieu_cao
        self.chu_vi = chu_vi
        self.dien_tich = dien_tich

    # Luật 1: Nếu biết 3 cạnh -> Tính được chu vi
    def tinh_chu_vi(self):
        if self.a is not None and self.b is not None and self.c is not None:
            self.chu_vi = self.a + self.b + self.c
            return self.chu_vi
        return "Không đủ dữ kiện tính chu vi."

    # Luật 2: Nếu biết cạnh đáy và chiều cao -> Tính được diện tích
    def tinh_dien_tich(self):
        if self.canh_day is not None and self.chieu_cao is not None:
            self.dien_tich = (self.canh_day * self.chieu_cao) / 2
            return self.dien_tich
        return "Không đủ dữ kiện tính diện tích."

    # Luật 3: Tính chiều cao ngược lại từ diện tích và cạnh đáy
    def tim_chieu_cao(self):
        if self.dien_tich is not None and self.canh_day is not None:
            self.chieu_cao = (self.dien_tich * 2) / self.canh_day
            return self.chieu_cao
        return "Không đủ dữ kiện tìm chiều cao."


# ==========================================
# BIỂU DIỄN TRI THỨC TOÁN TAM GIÁC LỚP 7
# ==========================================
class TamGiacLop7:
    """
    Biểu diễn tri thức tam giác lớp 7: Tập trung vào Định lý tổng 3 góc và Các trường hợp bằng nhau.
    Các Fact: 3 cạnh (AB, BC, CA) và 3 góc (A, B, C).
    """
    def __init__(self, ten="ABC", AB=None, BC=None, CA=None, goc_A=None, goc_B=None, goc_C=None):
        self.ten = ten
        self.AB = AB
        self.BC = BC
        self.CA = CA
        self.goc_A = goc_A
        self.goc_B = goc_B
        self.goc_C = goc_C
        self.chuan_hoa_goc()

    # Luật 1: Tổng 3 góc trong một tam giác bằng 180 độ. Từ đó suy ra góc còn lại.
    def chuan_hoa_goc(self):
        goc_da_biet = [g for g in [self.goc_A, self.goc_B, self.goc_C] if g is not None]
        if len(goc_da_biet) == 2:
            tong_2_goc = sum(goc_da_biet)
            goc_con_lai = 180 - tong_2_goc
            if self.goc_A is None: self.goc_A = goc_con_lai
            elif self.goc_B is None: self.goc_B = goc_con_lai
            elif self.goc_C is None: self.goc_C = goc_con_lai

def kiem_tra_bang_nhau(tg1: TamGiacLop7, tg2: TamGiacLop7):
    """
    Hệ chuyên gia mini kiểm tra 2 tam giác bằng nhau dựa trên các định lý Lớp 7.
    """
    # Luật 2: Cạnh - Cạnh - Cạnh (c-c-c)
    if None not in (tg1.AB, tg1.BC, tg1.CA, tg2.AB, tg2.BC, tg2.CA):
        if (tg1.AB == tg2.AB and tg1.BC == tg2.BC and tg1.CA == tg2.CA):
            return "Hai tam giác bằng nhau theo trường hợp: Cạnh - Cạnh - Cạnh (c.c.c)"

    # Luật 3: Cạnh - Góc - Cạnh (c-g-c)
    # Giả sử xét cặp: (AB, góc B, BC)
    if None not in (tg1.AB, tg1.goc_B, tg1.BC, tg2.AB, tg2.goc_B, tg2.BC):
        if (tg1.AB == tg2.AB and tg1.goc_B == tg2.goc_B and tg1.BC == tg2.BC):
            return "Hai tam giác bằng nhau theo trường hợp: Cạnh - Góc - Cạnh (c.g.c)"
            
    # Luật 4: Góc - Cạnh - Góc (g-c-g)
    # Giả sử xét cặp: (góc A, AB, góc B)
    if None not in (tg1.goc_A, tg1.AB, tg1.goc_B, tg2.goc_A, tg2.AB, tg2.goc_B):
        if (tg1.goc_A == tg2.goc_A and tg1.AB == tg2.AB and tg1.goc_B == tg2.goc_B):
            return "Hai tam giác bằng nhau theo trường hợp: Góc - Cạnh - Góc (g.c.g)"

    return "Không đủ điều kiện để kết luận hai tam giác bằng nhau."


# ==========================================
# CHẠY THỬ NGHIỆM (TESTING)
# ==========================================
if __name__ == "__main__":
    print("--- TEST BÀI TOÁN LỚP 5 ---")
    # Bài toán: Cho tam giác có cạnh đáy 13cm, chiều cao 4.6cm. Tính diện tích.
    tg_lop5 = TamGiacLop5(canh_day=13, chieu_cao=4.6)
    print(f"Diện tích tam giác lớp 5 là: {tg_lop5.tinh_dien_tich()} cm2")

    print("\n--- TEST BÀI TOÁN LỚP 7 ---")
    # Bài toán: Cho 2 tam giác ABC và DEF. 
    # Tam giác ABC có AB=5, AC=6, BC=7
    # Tam giác DEF có DE=5, DF=6, EF=7
    tg_ABC = TamGiacLop7(ten="ABC", AB=5, BC=7, CA=6)
    tg_DEF = TamGiacLop7(ten="DEF", AB=5, BC=7, CA=6) # Giả lập DE ứng với AB, EF ứng với BC...
    
    ket_qua_ccc = kiem_tra_bang_nhau(tg_ABC, tg_DEF)
    print(f"Kiểm tra tam giác ABC và DEF: {ket_qua_ccc}")

    # Bài toán: Cho tam giác MNP có góc M = 50 độ, góc N = 60 độ. Tìm góc P.
    tg_MNP = TamGiacLop7(ten="MNP", goc_A=50, goc_B=60) # Map M->A, N->B, P->C
    print(f"Góc còn lại của tam giác MNP là: {tg_MNP.goc_C} độ (Được nội suy tự động)")