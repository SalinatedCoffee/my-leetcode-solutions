## 2485. (E) Find the Pivot Integer

### `solution.py`
As is quite often the case for easy problems, there exists a variety of ways that this problem can be solved also. We will cover most of them, in descending order of their time complexity.  
The brute force method would be to simply try all possible pivots, where the sum of the left and right sides are incrementally computed every time. This is obviously not optimal, and such an algorithm would have a quadratic time complexity. We can do much better by performing some kind of precomputation so that we can calculate the left and right sums in constant time. This can be achieved by using prefix sums. If `pre[i]` is the sum of all integers from `1` to `i`, the left sum is `pre[i]` and the right is `pre[n] - pre[i-1]` if `i` is the pivot. Both expressions can be evaluated in constant time, making the algorithm much faster than the brute force approach. If no `i` exists in the range `[1, n]` such that `pre[i] == pre[n] - pre[i-1]`, we return `-1` as described by the problem.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is `n`. We try all integers in the range `[1, n]`, with each check taking constant time to perform. Prefix sums for all integers in the aforementioned range is kept in memory, hence the linear space complexity.  
  


### `solution_2.py`
The previous solution can be improved upon by realizing that the search space is monotonic, which allows us to utilize binary search. Some potential pivot `i` can fall under one of three difference cases. Either the left and right side sums are equal, or the left side is larger, or the right side is larger. When the left side is larger, we know that we should search for the actual pivot (if it exists) in the left side of `i`. The same logic can be used to determine when to search in the right side as well. To compute the left and right side sums, we could use the same prefix sum method used in the previous solution. However, we can also compute these values without any precomputation by utilizing the formula $n(n+1)/2$, which results in the sum of all integers in the range $[1, n]$.  

#### Conclusion
The time complexity of this solution is $O(\log n)$. Binary search essentially halves the search space at every iteration, hence the logarithmic time complexity. The space complexity is $O(1)$.  
  


### `solution_3.py`
We can do *even better* by simply writing an equation and solving for the unknown. Using the formulas used in the previous solution, we can say that the sum of the left side for some pivot $x$ is $x(x+1)/2$ and the right side $(n-x)(n-x+1)/2 + x(n-x) + x$. We want to solve for $x$ when these two expressions are equal, so we can simplify $x(x+1)/2 = (n-x)(n-x+1)/2 + x(n-x) + x$ to see whether $x$ can be easily computed.  
$$
x(x+1)/2 = (n-x)(n-x+1)/2 + x(n-x) + x \\[5pt]
x(x+1) = (n-x)(n-x+1) + 2x(n-x) + 2x \\[5pt]
x^2+x = n^2-nx+n-nx+x^2-x + 2nx-2x^2 + 2x \\[5pt]
0 = n^2+n-2x^2 \\[5pt]
x^2 = (n^2+n)/2 \\[5pt]
x = \sqrt{(n^2+n)/2}
$$
$n$ is simply `n`, and so we can compute $x$ and verify whether if it is an integer. If it is, than $x$ is the pivot. Otherwise, a pivot does not exist, so we return `-1`.  

#### Conclusion
This solution has a time and space complexity of $O(1)$. The point of contention is whether `sqrt` runs in constant time or logarithmic time. The algorithm for computing a square root of a number does indeed run in logarithmic time. However, most hardware can compute square roots in a fixed number of CPU cycles, making it a constant time operation.  
  

