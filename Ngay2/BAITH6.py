S = input("Nhập chuỗi S: ")
# Nhập từ cần đếm
word_to_find = input("Nhập từ cần tìm (word): ")
words_list = S.lower().split()
count = words_list.count(word_to_find.lower())
print(f"Số từ {word_to_find} là {count}")