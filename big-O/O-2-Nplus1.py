def all_fib(n):
    for i in range(n):
        print(fib(i))

def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

all_fib(10)

# Complexity: O(2 ^ (n+1))
# all_fib function
## For each value from 0 to n-1, it calls the fib function. 
### Within the fib function, the recursion tree expands exponentially.
### When fib(n) is called, it calls fib(n-1) and fib(n-2), 
### and each of those calls, in turn, calls two more fib functions, and so on. 
### This branching continues until it reaches the base cases of fib(0) and fib(1).

# The number of function calls in the recursion tree follows 
# a binary tree pattern, 
# where each level has twice as many nodes as the previous level. 
# So, the total number of function calls made by the fib function 
# for a given n can be approximated as 2^(n+1).


