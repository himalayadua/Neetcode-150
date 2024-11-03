def maximize_revenue_greedy(R):
    n = len(R)  # Length of the input revenue array
    stores = []  # List to store the indices where stores are opened
    last_store_index = -4  # Initialize to a value that allows placing a store at the first valid position

    # Iterate through each block in the revenue array
    for i in range(n):
        # Check if a store can be opened at block i and respect the spacing constraint
        if R[i] > 0 and i - last_store_index > 3:
            stores.append(i)  # Open a store at block i
            last_store_index = i  # Update the last store index
    
    total_revenue = sum(R[i] for i in stores)  # Calculate total revenue from opened stores
    return total_revenue, stores  # Return the total revenue and the list of opened store indices

# Example dataset to test the function
R = [0, 10, 0, 0, 50, 0, 0, 0, 100]  # Expected revenue for each block
result = maximize_revenue_greedy(R)
print("Total Revenue:", result[0])
print("Stores opened at blocks:", result[1])
