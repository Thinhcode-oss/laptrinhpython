import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    numbers = []
    
    # 1. Vong lap cho nguoi dung nhap du lieu
    while True:
        try:
            num = int(input("Nhap mot so nguyen: "))
            numbers.append(num)
        except ValueError:
            print("Vui long nhap mot so nguyen hop le!")
            continue
            
        choice = input("Ban co muon tiep tuc nhap khong? (Y/N): ").strip().upper()
        if choice == 'N' or choice == 'NO':
            break
    
    # Xu ly truong hop nguoi dung chua nhap gi da thoat
    if not numbers:
        print("Danh sach trong. Khong co gi de xu ly.")
        return

    print("\n" + "="*30)
    print(f"Danh sach ban vua nhap: {numbers}")

    # a) In ra cac so nguyen to co trong list
    primes = [n for n in numbers if is_prime(n)]
    print(f"\na) Cac so nguyen to trong list: {primes if primes else 'Khong co'}")

    # b) Tinh trung binh cong cac so am, trung binh cac so duong
    positives = [n for n in numbers if n > 0]
    negatives = [n for n in numbers if n < 0]
    
    avg_pos = sum(positives) / len(positives) if positives else 0
    avg_neg = sum(negatives) / len(negatives) if negatives else 0
    
    print(f"b) Trung binh cong cac so duong: {avg_pos}")
    print(f"   Trung binh cong cac so am: {avg_neg}")

    # c) So lon nhat, so nho nhat
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"c) So lon nhat: {max_num}")
    print(f"   So nho nhat: {min_num}")

    # d) Cho biet cac so trong list co duoc sap xep tang dan hay chua?
    # So sanh list hien tai voi mot ban sao da duoc sap xep cua chinh no
    is_sorted = numbers == sorted(numbers)
    if is_sorted:
        print("d) Cac so trong list DA duoc sap xep tang dan.")
    else:
        print("d) Cac so trong list CHUA duoc sap xep tang dan.")

if __name__ == "__main__":
    main()