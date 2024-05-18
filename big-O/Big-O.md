# Big O

Big-O complexity can be visualized with this graph:
![The Big-O](https://i.sstatic.net/WcBRI.png "Big-O")

Big-O notation is a `relative` `representation` of the `complexity` of an algorithm.
- relative
    - you can only compare apples to apples. 
    - a comparison of two algorithms that does similar work.
- representation
    - reduces the comparison between algorithms to a single variable.
- complexity
    - how many CPU cycles required to solve a problem when compared to a simpler problem


# Example
- Arithmetic
    - Take two numbers (123456 and 789012). 
    - A basic arithmetic operations: addition
    - It is an operation or a problem. 
    - A method of solving these is called an algorithm.

- 10000 + 20000
    - 5 addition operations
- 100 digit number + 100 digit number
    - 100 addition operations
- 10,000 digit number + 10,000 digit number
    - 10,000 addition operations

> complexity (being the number of operations) is directly proportional to the number of digits n in the larger number. 
>> We call this O(n) or linear complexity.


- Logarithmic
    - as the input size increases, the execution time increases, but at a much slower rate compared to linear growth.
    - increase in execution time is not proportional to number of elements.
- Example
    - Algorithm takes 1 second to process 100 elements
    - takes 2 seconds to process 10,000 elements
- In algorithms with a time complexity of O(log n), such as binary search, the array size is typically reduced by half at each iteration. This reduction happens because these algorithms are designed to divide the search space in half at each step, allowing for efficient searching or processing of elements.

- Another example
    - let's consider a sorted array of size n. 
    - In the first iteration of a binary search, you compare the target value with the middle element of the array. 
    - If the middle element is equal to the target, the search is complete. 
    - Otherwise, if the target is smaller, you can eliminate the upper half of the array. 
    - If the target is larger, you can eliminate the lower half of the array. 
    - This process of dividing the search space in half continues until the target value is found or until the search space becomes empty.

> At each iteration, the size of the remaining search space is halved. This logarithmic reduction in the search space is what leads to the logarithmic time complexity of O(log n). As a result, even with a large input size, the number of iterations required to find the target value remains relatively small.









| Big O Notation | Type        | Computations for 10 elements | Computations for 100 elements | Computations for 1000 elements |
| -------------- | ----------- | ---------------------------- | ----------------------------- | ------------------------------ |
| **O(1)**       | Constant    | 1                            | 1                             | 1                              |
| **O(log N)**   | Logarithmic | 3                            | 6                             | 9                              |
| **O(N)**       | Linear      | 10                           | 100                           | 1000                           |
| **O(N log N)** | n log(N)    | 30                           | 600                           | 9000                           |
| **O(N^2)**     | Quadratic   | 100                          | 10000                         | 1000000                        |
| **O(2^N)**     | Exponential | 1024                         | 1.26e+29                      | 1.07e+301                      |
| **O(N!)**      | Factorial   | 3628800                      | 9.3e+157                      | 4.02e+2567                     |

### Data Structure Operations Complexity

| Data Structure         | Access | Search | Insertion | Deletion |
| ---------------------- | :----: | :----: | :-------: | :------: |
| **Array**              |   1    |   N    |     N     |    N     |
| **Stack**              |   N    |   N    |     1     |    1     |
| **Queue**              |   N    |   N    |     1     |    1     |
| **Linked List**        |   N    |   N    |     1     |    N     |
| **Hash Table**         |   1    |   N    |     N     |    N     |
| **Binary Search Tree** |   N    |   N    |     N     |    N     |