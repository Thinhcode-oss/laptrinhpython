# Nhap so tien X tu ban phim
try:
    X = int(input("Nhap so tien X: "))
    original_X = X
    
    # Danh sach cac menh gia tien theo thu tu giam dan
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    total_bills = 0
    results = []

    print(f"\nSo tien {original_X} duoc doi thanh:")

    # Duyet qua tung menh gia
    for coin in denominations:
        # Tinh so to tien cua menh gia hien tai
        count = X // coin
        # Cap nhat so tien con lai sau khi da doi
        X = X % coin
        
        results.append((coin, count))
        total_bills += count
        print(f"Loai {coin} gom {count} to")

    print("-" * 20)
    print(f"TONG CONG CO {total_bills} TO")

except ValueError:
    print("Vui long nhap mot so nguyen hop le!")