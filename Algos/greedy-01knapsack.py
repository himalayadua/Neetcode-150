def zero_one_knapsack(weights, profits, capacity):
    n = len(profits)
    # Create a 2D DP table where dp[i][w] represents the maximum profit for i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Max of including or excluding the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profits[i - 1])
            else:
                # If current item can't be included, take previous result
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Given data
profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
m = 15

# Calculate maximum value for 0/1 knapsack
zero_one_value = zero_one_knapsack(weights, profits, m)
print(zero_one_value)
