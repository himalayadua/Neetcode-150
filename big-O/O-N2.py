def print_pairs(array):
    for i in array:
        for j in array:
            print("%d, %d" %(i, j))

print_pairs([1, 2, 3, 4, 5])

# The complexity of the print_pairs function is: O(N^2)
# We do a nested loop = length(array) ^ 2 = N * 2
# There are O(N^2) pairs
# Conclusion: O(N^2)


def print_unordered_pairs(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            print("%d, %d" %(array[i], array[j]))

print_unordered_pairs([1, 2, 3, 4, 5])

# The complexity of the print_unordered_pairs function is: O(N^2)
# We do a nested loop = length(array) * (length(array) - 1) / 2 = (length(array) * 2 - length(array)) / 2 = (N^2 - N) / 2
# There are O((N^2 - N) / 2) pairs
# Conclusion: O(N^2)


def print_unordered_pairs(array_a, array_b):
    for a in array_a:
        for b in array_b:
            for i in range(1000000):
                print('%d, %d' %(a, b))

print_unordered_pairs([1, 2, 3, 4, 5], [3, 1, 2, 5, 4])

# The complexity of the print_unordered_pairs function is: O(N^2)
# We do a nested loop = length(array_a) * length(array_b) * 1000000 = N^2 * 1000000
# There are O(N^2 * 1000000) pairs
# Conclusion: O(N^2)