# coin change calculator

def min_coins(S, C):
    cache = [float('inf')] * (S+1)
    
    cache[0] = 0
    
    for i in range(1, S+1):
        for coin in C:
            if (i - coin) >= 0:
                cache[i] = min(cache[i], cache[i-coin] + 1)
    
    return cache[S] if cache[S] != float('inf') else -1

S = 6
C = [1,2,3,4,5,6]

print(f"you need {min_coins(S, C)} coins to make a total of {S}")


# [0, 1, inf, inf, inf, inf, inf]
# [0, 1, inf, inf, inf, inf, inf]
# [0, 1, inf, inf, inf, inf, inf]
# [0, 1, 2, inf, inf, inf, inf]
# [0, 1, 2, inf, inf, inf, inf]
# [0, 1, 2, inf, inf, inf, inf]
# [0, 1, 2, 3, inf, inf, inf]
# [0, 1, 2, 1, inf, inf, inf]
# [0, 1, 2, 1, inf, inf, inf]
# [0, 1, 2, 1, 2, inf, inf]
# [0, 1, 2, 1, 2, inf, inf]
# [0, 1, 2, 1, 2, inf, inf]
# [0, 1, 2, 1, 2, 3, inf]
# [0, 1, 2, 1, 2, 3, inf]
# [0, 1, 2, 1, 2, 1, inf]
# [0, 1, 2, 1, 2, 1, 2]
# [0, 1, 2, 1, 2, 1, 2]
# [0, 1, 2, 1, 2, 1, 2]
# you need 2 coins to make a total of 6

# ctrl + /  comment all lines together