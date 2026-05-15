def khoi_phuc_chuoi(cipher_text):
    """
    Ham khoi phuc chuoi goc tu chuoi nen (cipher text).
    Quy tac: # + <so luong> + <ky tu> se duoc bung ra thanh <ky tu> lap lai <so luong> lan.
    """
    plain_text = ""
    i = 0
    n = len(cipher_text)
    
    while i < n:
        # Neu gap ky tu danh dau '#'
        if cipher_text[i] == '#':
            # Lay so luong (nam ngay sau '#') va chuyen thanh so nguyen
            so_luong = int(cipher_text[i+1])
            
            # Lay ky tu can lap (nam sau so luong)
            ky_tu = cipher_text[i+2]
            
            # Them ky tu da duoc nhan ban vao chuoi ket qua
            plain_text += ky_tu * so_luong
            
            # Nhay buoc qua 3 ky tu (vi du: '#', '6', 'Z')
            i += 3
        else:
            # Neu la ky tu binh thuong, chi viec them vao ket qua
            plain_text += cipher_text[i]
            # Tien toi ky tu tiep theo
            i += 1
            
    return plain_text

cipher_1 = "XY#6Z1#4023"
plain_1 = khoi_phuc_chuoi(cipher_1)
print(f"Cipher text: {cipher_1}")
print(f"Plain text : {plain_1}")
print("-" * 30)

cipher_2 = "#39+1=1#30"
plain_2 = khoi_phuc_chuoi(cipher_2)
print(f"Cipher text: {cipher_2}")
print(f"Plain text : {plain_2}")