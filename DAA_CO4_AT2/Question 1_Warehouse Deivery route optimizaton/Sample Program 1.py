# Warehouse Delivery Route Optimization
# Using Prim's Algorithm (Greedy Strategy)

INF = float('inf')

# Graph represented using adjacency matrix
graph = [
    [9, 2, 4],
    [2, 7, 8],
    [8, 1, 4]
]

V = len(graph)

# Keep track of selected warehouses
selected = [False] * V
selected[0] = True

edges = 0
total_weight = 0

# MST contains V-1 edges
while edges < V - 1:

    minimum = INF

    # Find minimum cost edge
    # connecting selected and unselected vertices
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and graph[i][j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    # Add edge weight to MST
    total_weight += graph[x][y]

    selected[y] = True
    edges += 1

print("Total Weight of MST =", total_weight)

input("\n\npress enter to exit..")
