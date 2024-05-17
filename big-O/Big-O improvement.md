# Calculate all Fibonacci numbers till n

```python
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
```

> Complexity: O(2 ^ (n+1))

# Analysis
- all_fib function
    - For each value from 0 to n-1, it calls the fib function. 
- Within the fib function, the recursion tree expands exponentially.
    - When fib(n) is called, it calls fib(n-1) and fib(n-2), 
    - and each of those calls, in turn, calls two more fib functions, and so on. 
    - This branching continues until it reaches the base cases of fib(0) and fib(1).

# Conclusion
- The number of function calls in the recursion tree follows 
- a binary tree pattern
    - where each level has twice as many nodes as the previous level. 
    - So, the total number of function calls made by the fib function 
    - for a given n can be approximated as 2^(n+1).


# Flaws
- Redundant calculations
    - code recalculates Fibonacci numbers multiple times
    - leading to an exponential increase in the number of function calls.

# Improvement
- Solution
    - Use memoization to store previously calculated Fibonacci numbers 
    - to avoid redundant computations
    - Introduce a data structure, such as a list, to store the already computed Fibonacci numbers. 
    - This allows the code to check if a value is already available before performing recursive calculations.


# Solution
- Memoization
    - store the results of expensive function calls 
    - reuses them when the same inputs occur again
    - rather than recomputing the results.

```python
def all_fib(n):
    memo = []
    memo.append(0)
    memo.append(1)

    for i in range(n):
        print("%d: %d" %(i, fib(i, memo)))

def fib(n, memo):
    if n <= len(memo) - 1:
        return memo[n]

    memo.append(fib(n - 1, memo) + fib(n - 2, memo))
    return memo[n]

all_fib(7)
```

# Complexity: O(N)
**All previous actions are already computed**

**Explaination**
- Check    
    - the fib function first checks if the result for that index is already available in the memo list. 
    - If it is, the function simply returns the precomputed value, avoiding the need for redundant computation.
- Calculate
    - If the result is not found in the memo list
    - the function proceeds with the recursive calculation
    - It calls itself for indices n-1 and n-2 and passes the memo list along
- Re-Check
    - If the result for either of those indices is not available in the memo list
    - it recursively calculates it until all necessary Fibonacci numbers are computed
    - The computed values are stored in the memo list for future use.

> The code is now more efficient for larger values of n.
>> The updated code with memoization improves the time complexity of the Fibonacci number calculation from exponential (O(2^(n+1))) to linear (O(n)).

