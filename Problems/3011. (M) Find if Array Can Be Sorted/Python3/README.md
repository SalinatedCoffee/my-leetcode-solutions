## 3011. (M) Find if Array Can Be Sorted

### `solution.py`
Given the list of integers `nums`, we are asked to determine whether `nums` can be sorted using the following rule:  

- Adjacent values can be swapped if their binary representations have the same number of set bits.  

Because we are only allowed to swap *adjacent* values with the same number of set bits, we can immediately see that the relative order of elements with different numbers of set bits cannot be changed. That is, we can think of `nums` as being comprised of multiple intervals, with each interval corresponding to some number of set bits. When examining two adjacent intervals, we would want the largest value of the left interval to be less than or equal to the smallest value of the right interval. Intuition tells us that we could achieve this by implementing a sliding window based algorithem, where the window is expanded if the current element has the same number of raised bits as those currently in the window. If not, we compare the largest element from the previous window and the smallest element in the current window before resetting the current window so that it only includes the current element. If the comparison evaluates to `False`, `nums` cannot be sorted using the given rule and we return `False` as well. Otherwise, we examine the last interval after the loop exits and return the appropriate value.  

#### Conclusion
This solution has a time complexity of $O(n\log k)$, where $n$ is the length of `nums` and `k` is the average length of the binary representation of the elements in `nums`. Each and every element of `nums` is examined, and counting the number of raised bits of an integer with `d` binary digits requires $O(\log d)$ time. Hence, the overall time complexity of this solution is $O(n\log k)$. The space complexity is $O(1)$.  
  

