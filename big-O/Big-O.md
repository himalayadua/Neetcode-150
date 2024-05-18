# Big O

## Let's explore the concept of Big-O notation at different levels of complexity:

### For a 5-year-old kid:
Imagine you have a box of crayons and you want to find your favorite blue one. 
- If you have only a few crayons, you can find it really fast! 
- But if you have a huge box with hundreds of crayons, it will take you much longer. 
- Big-O is like a game where we guess how long it will take to find the crayon as the box gets bigger and bigger.

### For a school student:
Big-O notation is a way to measure how fast a computer program runs 
- but instead of using seconds, we use the number of steps it takes. 
- Think of it like a recipe: some recipes take more steps and are more complicated, especially if you're making a big cake for a lot of people. 
- Big-O tells us how the number of steps grows when the amount of stuff the program has to work with gets bigger.

### For a computer science college student:
Big-O notation is a mathematical concept used in Computer Science to describe the performance or complexity of an algorithm. 
- it describes the worst-case scenario of how an algorithm's run time or space requirements grow as the input size increases. 
- example
    - a linear search algorithm has a Big-O of `O(n)` 
    - because its performance is directly proportional to the size of the data set.

### For a software engineer preparing for a coding interview:
Big-O notation is crucial for evaluating the efficiency of an algorithm. 
- It helps you understand 
    - the time complexity (like how long an algorithm takes to run) and 
    - space complexity (how much memory it uses) in terms of input size. 
- For instance
    - an efficient sorting algorithm like quicksort has an average-case complexity of `O(n log n)`
    - which means it can handle large data sets relatively quickly.

### For a PhD student in algorithms:
Big-O notation is a fundamental aspect of algorithmic analysis, providing a high-level abstraction of algorithmic efficiency. 
- It encapsulates the asymptotic upper bound of the growth rate of 
    - the runtime or space complexity as a function of input size, 
    - abstracting away constants and lower-order terms. 
- When analyzing algorithms, you'll consider Big-O for 
    - both average-case and worst-case scenarios, and 
    - you'll often deal with trade-offs between time and space complexity. 
- Advanced topics might include amortized analysis, complexity classes, and exploring the lower bounds of problems to understand the theoretical limits of algorithmic optimization.

## Big-O complexity can be visualized with this graph:
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