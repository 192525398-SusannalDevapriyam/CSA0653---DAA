# Investment Portfolio Optimization
# Dynamic Programming (0/1 Knapsack)

capital = [20000, 30000, 40000, 50000]
returns = [25000, 40000, 50000, 70000]

investments = ["A", "B", "C", "D"]

budget = 80000

# Convert values to units of 1000
budget = budget // 1000
weights = [c // 1000 for c in capital]

n = len(investments)

# DP Table
dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

# Fill DP table
for i in range(1, n + 1):
    for w in range(1, budget + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                returns[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Find selected investments
selected = []
w = budget

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected.append(investments[i - 1])
        w -= weights[i - 1]

selected.reverse()

print("\nSelected Investments:", selected)
print("\nMaximum Return = Rs.", dp[n][budget])

input("\n\npress enter to exit...")
