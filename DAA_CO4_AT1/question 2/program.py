# 192525398 - S.Susannal Devapriyam


# Kruskal's Algorithm using Disjoint Set

class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n))

    # Find parent of a vertex
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # Union two sets
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)


# Graph edges (u, v, weight)
edges = [
    (0, 1, 2),
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 4),
    (2, 3, 5)
]

vertices = 4

# Sort edges based on weight
edges.sort(key=lambda x: x[2])

ds = DisjointSet(vertices)

mst_cost = 0

# Select edges one by one
for u, v, w in edges:

    # Avoid cycle formation
    if ds.find(u) != ds.find(v):
        ds.union(u, v)
        mst_cost += w

# Display only total cost
print("Total Cost of MST =", mst_cost)


input("\n\n press enter to exit")
