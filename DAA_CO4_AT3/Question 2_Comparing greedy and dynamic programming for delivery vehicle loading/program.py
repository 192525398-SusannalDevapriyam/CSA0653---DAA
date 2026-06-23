# Delivery Vehicle Loading
# 0/1 Knapsack using Dynamic Programming

weights = [10, 20, 30, 25]
profits = [60, 100, 120, 110]

packages = ["P1", "P2", "P3", "P4"]

capacity = 50
n = len(packages)

# DP Table
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Fill DP Table
for i in range(1, n + 1):
    for w in range(capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Find selected packages
selected = []
w = capacity

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(packages[i - 1])
        w -= weights[i - 1]

selected.reverse()

print("\nSelected Packages:", selected)
print("\n\nMaximum Profit =", dp[n][capacity])

input("\n\n\npress enter toexit...")