

# Manufacturing Resource Allocation
# Using Dynamic Programming (0/1 Knapsack)

# Product investments and profits
investments = [20000, 30000, 40000, 50000]
profits = [25000, 40000, 50000, 65000]

products = ["A", "B", "C", "D"]

budget = 100000
n = len(products)

# Convert values to units of 1000
budget = budget // 1000
weights = [i // 1000 for i in investments]

# DP Table
dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

# Build DP table
for i in range(1, n + 1):
    for w in range(1, budget + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Find selected products
selected = []
w = budget

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(products[i - 1])
        w -= weights[i - 1]

selected.reverse()

print("Selected Products:", selected)
print("\nMaximum Profit = Rs.", dp[n][budget])

input("\n\npress enter to exit...")