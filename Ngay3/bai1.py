import math

# a) Trả về trị tuyệt đối của n
absolute_val = lambda n: abs(n)

# b) Trả về giá trị n + 15
add_15 = lambda n: n + 15

# c) Trả về tích của x và y
multiply = lambda x, y: x * y

# d) Kiểm tra n có là bội số của 13 hoặc 19 hay không
is_multiple_13_19 = lambda n: n % 13 == 0 or n % 19 == 0

# e) Tính diện tích hình tròn (S = pi * r^2)
circle_area = lambda r: math.pi * r**2

# f) Tính chu vi hình chữ nhật (P = (d + r) * 2)
rect_perimeter = lambda d, r: (d + r) * 2

# g) Kiểm tra n có phải số chính phương hay không
is_perfect_square = lambda n: n >= 0 and (n**0.5).is_integer()

# h) Kiểm tra n có là số nguyên tố hay không
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# i) Kiểm tra 3 cạnh tam giác và loại tam giác
check_triangle = lambda a, b, c: (
    "Không phải tam giác" if not (a + b > c and a + c > b and b + c > a) else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or b == c or a == c) else
    "Tam giác cân" if a == b or b == c or a == c else
    "Tam giác vuông" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác thường"
)

# --- TEST THỬ CÁC HÀM ---
print(f"a) Tuyệt đối của -5: {absolute_val(-5)}")
print(f"b) 10 + 15: {add_15(10)}")
print(f"c) 5 * 6: {multiply(5, 6)}")
print(f"d) 38 có chia hết cho 13 hoặc 19? {is_multiple_13_19(38)}")
print(f"e) Diện tích hình tròn r=3: {circle_area(3):.2f}")
print(f"f) Chu vi HCN 4x5: {rect_perimeter(4, 5)}")
print(f"g) 16 là số chính phương? {is_perfect_square(16)}")
print(f"h) 17 là số nguyên tố? {is_prime(17)}")
print(f"i) Bộ ba (3, 4, 5) là: {check_triangle(3, 4, 5)}")
print(f"i) Bộ ba (5, 5, 5) là: {check_triangle(5, 5, 5)}")