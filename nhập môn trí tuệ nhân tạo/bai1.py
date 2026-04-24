# ============================================
# LAB 2 - BAI TOAN TO MAU DO THI
# Thuat toan: Largest Degree First (Heuristic)
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
def select_vertex(color, d, n):
    max_d = -1
    s = -1
    for i in range(n):
        if color[i] == -1 and d[i] > max_d:
            max_d = d[i]
            s = i
    return s
def assign_color(s, graph, color, used_colors, n):
    for c in range(used_colors):
        allowed = True 
        for neighbor in range(n):
            if graph[s][neighbor] == 1 and color[neighbor] == c:
                allowed = False
                break
        
        if allowed:
            color[s] = c
            return used_colors 

    color[s] = used_colors
    return used_colors + 1
def reduce_degree(s, graph, color, d, n):
    d[s] = -1
    # --- Code bo sung ---
    for i in range(n):
        if graph[s][i] == 1 and color[i] == -1:
            d[i] -= 1 

def graph_coloring(graph, n):
    color = [-1] * n
    d = [0] * n

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                d[i] += 1
                
    used_colors = 0

    print("Initial d:", d)
    print("Initial color:", color)
    print("-" * 20)
    
    for step in range(n):
        s = select_vertex(color, d, n)
        used_colors = assign_color(s, graph, color, used_colors, n)
        reduce_degree(s, graph, color, d, n)
        print(f"Step {step + 1} (Chon dinh {s}):")
        print("d:", d)
        print("color:", color)

    return color, used_colors

colors, k = graph_coloring(graph, n)
print("=" * 40)
print("KET QUA CUOI CUNG")
print("So mau dung:", k) 
print("-" * 40)
print("Cach to:", colors)
print("=" * 40)