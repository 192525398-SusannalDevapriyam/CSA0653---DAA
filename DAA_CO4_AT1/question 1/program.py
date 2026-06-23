# 192525398 - S.Susannal Devapriyam


# Prim's Algorithm to find Minimum Spanning Tree

INF = float('inf')

# Adjacency matrix representation of graph
graph = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]

V = len(graph)

# Track selected vertices
selected = [False] * V
selected[0] = True

edges = 0
total_weight = 0

# MST contains V-1 edges
while edges < V - 1:

    minimum = INF

    # Find minimum edge connecting
    # selected and unselected vertices
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if (not selected[j]) and graph[i][j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    # Add edge weight to MST cost
    total_weight += graph[x][y]
    selected[y] = True
    edges += 1

# Display only total weight
print("Total Weight of MST =", total_weight)

input("\n\n press enter to exit...")
