def powers_of_2(n):
    if n <= 0:
        return 0

    if n == 1:
        print(1)
        return 1

    previous = powers_of_2(n / 2)
    current = previous * 2
    print(current)
    return current

powers_of_2(4)

# Complexity: O(log N)





def sqrt(n):
    return sqrt_helper(n, 1, n)

def sqrt_helper(n, min, max):
    if min > max:
        return -1

    guess = (min + max) / 2

    if guess * guess > n:
        return sqrt_helper(n, min, guess - 1)
    elif guess * guess < n:
        return sqrt_helper(n, guess + 1, max)
    else:
        return guess

print(sqrt(100))
print(sqrt(9))
print(sqrt(25))
print(sqrt(3))

# Complexity: O(log N) --> It is a binary search algorithm




from math import sqrt

def square_root(n):
    for guess in range(int(sqrt(n))+1):
        if guess * guess == n:
            return guess

    return -1

print(square_root(100))
print(square_root(9))
print(square_root(25))
print(square_root(3))

# Complexity: O(log N) --> It is a binary search algorithm