# ============================================
# LAB 2 - BAI TOAN TO MAU DO THI
# Thuat toan: Largest Degree First (DSatur)
# ============================================

# do thi co 10 dinh
n = 10
graph = [
    [0,1,1,1,0,0,0,0,0,0],  # 0
    [1,0,1,0,0,1,1,0,0,0],  # 1
    [1,1,0,1,0,1,0,0,0,0],  # 2
    [1,0,1,0,1,1,0,0,0,0],  # 3
    [0,0,0,1,0,0,0,0,1,0],  # 4
    [0,1,1,1,0,0,1,1,0,0],  # 5
    [0,1,0,0,0,1,0,1,0,1],  # 6
    [0,0,0,0,0,1,1,0,1,0],  # 7
    [0,0,0,0,1,0,0,1,0,1],  # 8
    [0,0,0,0,0,0,1,0,1,0],  # 9
]
# note:
# - graph[i][j] = 1 => i ke j
# - graph[i][j] = 0 => i khong ke j

#--------------------------------------#
# ham chon dinh de to mau
def select_vertex(color, d, n):
    max_d = -1
    s = -1
    # sinh vien bo sung noi dung
    return s
#--------------------------------------#

#--------------------------------------#
# ham chon mau cho dinh s
def assign_color(s, graph, color, used_colors, n):
    # sinh vien bo sung noi dung
    color[s] = used_colors
    return used_colors + 1
#--------------------------------------#

#--------------------------------------#
# Ham giam bac cac dinh ke cua dinh s
def reduce_degree(s, graph, color, d, n):
    d[s] = -1
    # sinh vien bo sung noi dung
#--------------------------------------#

# Ham thuc thi
def graph_coloring(graph, n):
    color = [-1] * n
    d = [0] * n

    # Khoi tao bac
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                d[i] += 1
                
    # So luong mau da su dung
    used_colors = 0

    print("d:", d)
    print("color", color)
    for _ in range(n):
        # -------------------------------
        # Buoc 1: Chon dinh s chua to co d[s] lon nhat
        s = select_vertex(color, d, n)
        # -------------------------------
        
        # -------------------------------
        # Buoc 2: Chon mau phu hop
        used_colors = assign_color(s, graph, color, used_colors, n)
        # -------------------------------
        
        # -------------------------------
        # Buoc 3: giam bac cac dinh ke s
        reduce_degree(s, graph, color, d, n)
        # -------------------------------
        
        print("d:", d)
        print("color:", color)

    return color, used_colors

colors, k = graph_coloring(graph, n)
print("-" * 40)
print("So mau dung:", k)
print("-" * 40)
print("Cach to:", colors)
print("-" * 40)



