import re

def chuan_hoa_chuoi(s):
    # 1. Xử lý các dòng: Đảm bảo các dòng canh thẳng hàng (loại bỏ khoảng trắng đầu/cuối mỗi dòng)
    lines = [line.strip() for line in s.split('\n')]
    
    processed_lines = []
    for line in lines:
        if not line: # Bỏ qua dòng trống
            continue
            
        # 2. Giữa các từ chỉ cách nhau bởi 1 khoảng trắng
        # Dùng regex r'\s+' để thay thế mọi cụm khoảng trắng bằng 1 space duy nhất
        line = re.sub(r'\s+', ' ', line)
        
        # 3. Dấu chấm (.) và dấu phẩy (,) phải đi liền với từ trước nó
        # Tìm khoảng trắng đứng trước dấu chấm/phẩy và xóa đi
        line = re.sub(r'\s+([.,])', r'\1', line)
        
        # 4. Đảm bảo sau dấu chấm/phẩy có 1 khoảng trắng (nếu chưa có và chưa phải cuối dòng)
        line = re.sub(r'([.,])(?=[^\s])', r'\1 ', line)
        
        processed_lines.append(line)
    
    # Nối lại các dòng thành chuỗi hoàn chỉnh
    return '\n'.join(processed_lines)

# Kiểm tra với ví dụ trong ảnh
input_s = """    Quê  hương
Quê  hương  là   chùm  khế   ngọt .
   Cho  con  trèo  hái   mỗi   ngày   .  
Quê   hương  là   đường  đi  học . 
  Con  về  rọp  bướm  vàng  bay .
  Đỗ      Trung  Quân   """

ket_qua = chuan_hoa_chuoi(input_s)
print("--- Chuỗi hoàn chỉnh ---")
print(ket_qua)