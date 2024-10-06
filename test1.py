import matplotlib.pyplot as plt
import networkx as nx

# 创建一个有向图
G = nx.DiGraph()

# 添加节点
tables = [
    "adjust_room", "admin", "dorm_build", "dorm_manager",
    "dorm_room", "notice", "repair", "student", "visitor"
]
G.add_nodes_from(tables)

# 添加边（外键关系）
edges = [
    ("adjust_room", "student"),
    ("dorm_manager", "dorm_build"),
    ("dorm_room", "dorm_build"),
    ("repair", "dorm_build"),
    ("repair", "dorm_room")
]
G.add_edges_from(edges)

# 绘制图
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrowsize=20)
plt.title("ER Diagram of Database")
plt.show()
