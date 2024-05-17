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