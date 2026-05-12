import json

def giai_quyet_theo_mapping():
    file_goc = "fileName.txt"
    file_rut_gon = "reduced_data.json"
    
    # Nội dung mẫu từ ảnh
    noi_dung = """Thuyền và biển
Chỉ có thuyền mới hiểu
Biển mênh mông nhường nào
Chỉ có biển mới biết
Thuyền đi đâu về đâu"""

    with open(file_goc, "w", encoding="utf-8") as f:
        f.write(noi_dung)

    # --- (1) XUẤT RA FILE GIẢM DUNG LƯỢNG ---
    # Tách từ và giữ nguyên cả ký tự xuống dòng để khôi phục chính xác định dạng
    import re
    # re.findall sẽ tách cả từ và các ký tự đặc biệt/xuống dòng
    tokens = re.findall(r'\S+|\n', noi_dung)
    
    # Tạo danh sách các từ/ký tự duy nhất (từ điển)
    tu_dien = []
    for t in tokens:
        if t not in tu_dien:
            tu_dien.append(t)
            
    # Lưu vị trí xuất hiện của từng từ
    vi_tri_xuat_hien = [tu_dien.index(t) for t in tokens]
    
    # Lưu vào file JSON (để lưu cấu trúc danh sách)
    du_lieu_nen = {
        "dict": tu_dien,
        "map": vi_tri_xuat_hien
    }
    
    with open(file_rut_gon, "w", encoding="utf-8") as f:
        json.dump(du_lieu_nen, f, ensure_ascii=False)
        
    print(f"1. Đã lưu file giảm dung lượng: {file_rut_gon}")

    # --- (2) ĐỌC FILE VÀ TRẢ VỀ ĐỊNH DẠNG BAN ĐẦU ---
    with open(file_rut_gon, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    dictionary = data["dict"]
    mapping = data["map"]
    
    # Khôi phục bằng cách lấy từ trong từ điển theo vị trí đã lưu
    chuoi_khoi_phuc = ""
    for i in mapping:
        tu = dictionary[i]
        if tu == "\n":
            chuoi_khoi_phuc += tu
        else:
            # Thêm khoảng trắng sau mỗi từ, trừ khi từ tiếp theo là xuống dòng
            chuoi_khoi_phuc += tu + " "
    
    # Làm sạch khoảng trắng thừa ở cuối các dòng
    van_ban_cuoi = "\n".join([line.strip() for line in chuoi_khoi_phuc.split("\n")])

    print("\n2. Nội dung sau khi khôi phục ban đầu:")
    print("-" * 25)
    print(van_ban_cuoi)
    print("-" * 25)

if __name__ == "__main__":
    giai_quyet_theo_mapping()