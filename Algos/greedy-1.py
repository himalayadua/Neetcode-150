# Problem 1: Starbuck Locations

# As the head of Business Development at Starbucks, you are responsible for opening a series of Starbucks stores along Fifth Avenue in New York City.
# Think of this famous street as a straight line, consisting of n blocks numbered i = 1, 2, 3,..., n.

# Let A be an n-element array where each element is 0 or 1. If A[i] 1, then you are allowed to open a store on block i, and if A[i] = 0, then you are not allowed to open a store on block i.
# Given an input array A, your goal is to decide which stores to open, choosing among the values of i for which A[i] = 1. 
# The only condition you must meet is that each pair of stores must be separated by at least three blocks. 
# In other words, if you open stores on blocks x and y, then y − x >= 3.

# Your goal is to open as many stores as possible.

# For example, if n = 16 and A = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0], then the optimal solution is to open stores on blocks i = 2, 6, 10, 13,
#  as illustrated below with open stores in quotes:
# 0, "1", 0, 1, 0, "1", 0, 1, 0, "1", 0, 1, "1", 0, 0, 0

# (a) Provide a greedy algorithm to solve this problem. Clearly explain how your algorithm works, why the running time of your algorithm is O(n), 
# and show that the output is guaranteed to maximize the number of opened stores.

def maximize_stores(A):
    n = len(A)  # Length 
    stores = []  # which stores are opened
    last_store_index = -4  # first valid position
    

    for i in range(n):
        # condition to open store
        if A[i] == 1 and i - last_store_index >= 3:
            block_numbers = i + 1   # human readable block numbers
            stores.append(block_numbers)  
            last_store_index = i  
    
    return stores

# Example:
A = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0]
result = maximize_stores(A)
print("Stores opened at blocks:", result)


# Stores opened at blocks: [2, 6, 10, 13]


def maximize_stores(A):
    n = len(A)  # Length 
    stores = []  # which stores are opened
    last_store_index = -4  # first valid position
    

    for i in range(n):
        # condition to open store
        
        if A[i] == 1 and i - last_store_index >= 3:
            block_numbers = i + 1   # human readable block numbers
            stores.append(block_numbers)  
            print(f"i={block_numbers}, we can open a store since A[i]={A[i]}, and y-x={i - last_store_index}")
            last_store_index = i  
            
        else:
            block_numbers = i + 1   # human readable block numbers
            print(f"i={block_numbers}, we can't open a store since A[i]={A[i]}, and y-x={i - last_store_index}")
    
    return stores

# Example:

A = [0,0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1]
result = maximize_stores(A)
print("Stores opened at blocks:", result)

