def tim_so_con_thieu():
    s = input("Nhap so dien thoai (S): ")
    
    # Tao set chua cac ky tu tu '0' den '9'
    tat_ca_so = set("0123456789")
    
    # Tao set tu so dien thoai da nhap
    so_da_nhap = set(s)
    
    # Tim cac so khong xuat hien (phep hieu)
    ket_qua = sorted(list(tat_ca_so - so_da_nhap))
    
    print(f"Trong so dien thoai {s} khong chua cac ky so: {ket_qua}")

# Chay thu
tim_so_con_thieu()