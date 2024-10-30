def knapsack(S, W, P):
    n = len(W)
    cache = [0] * (S + 1)

    for i in range(n):
        for j in range(S, W[i] - 1, -1):
            cache[j] = max(cache[j], cache[j - W[i]] + P[i])
            print(cache)
    return cache[S]

S = 3
W = [1, 3, 5]
P = [1, 4, 6]

print(f"Maximum profit: {knapsack(S, W, P)}")