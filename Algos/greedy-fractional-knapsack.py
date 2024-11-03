def fractional_knapsack(weights, profits, capacity):
    # Calculate the value/weight ratio for each item
    index = list(range(len(profits)))
    ratio = [p/w for p, w in zip(profits, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)  # Sort by ratio in descending order

    max_value = 0  # Maximum value in knapsack

    for i in index:
        if weights[i] <= capacity:  # If the whole item can be added
            capacity -= weights[i]
            max_value += profits[i]
        else:  # Add the fractional part of the item
            max_value += profits[i] * (capacity / weights[i])
            break  # Knapsack is full

    return max_value

# Given data
n = 7
m = 15  # Capacity of the knapsack
profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]

# Calculate maximum value
max_value = fractional_knapsack(weights, profits, m)
print(max_value)

