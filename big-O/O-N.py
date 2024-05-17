def foo(array):
    sum = 0
    product = 1

    for element in array:
        sum += element

    for element in array:
        product *= element

    print("%d, %d" %(sum, product))

foo([1, 2, 3, 4, 5])

# The complexity of the foo function is: O(N)
# Initializing sum and product = 1 + 1 = 2
# We iterate through the array two times = 2 * length(array) = 2 * N
# Printing sum and product = 1
# Conclusion: O(2N + 3) = O(N)



def reverse(array):
    for i in range(len(array) // 2):
        index = len(array) - i - 1
        temporary_num = array[index]
        array[index] = array[i]
        array[i] = temporary_num

    return array

new_array = reverse (list(range(1, 6)))

for i in new_array:
    print(i)

# The complexity of the reverse function is: O(N)
# Even though we iterate only through half of the array (O(N/2)), we still consider this a O(N) complexity
# Conclusion: O(N)


# O(N + P), if P < N / 2 --> O(N)
# O(2N) --> O(N)
# O(N + logN) --> O(N)
# O(N + M), if N > M then O(N), otherwise O(M)

