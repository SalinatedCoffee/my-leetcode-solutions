## 342. (E) Power of Four

### `solution.py`
For a number to be a power of 4, it cannot be negative or `0`, which we can trivially check before doing anything else. If `n` is positive, we simply continue dividing it by four while it is larger than `1`, and if at any point the remainder of the division is non-zero, we can immediately return `False`.  

#### Conclusion
This solution has a time complexity of $O(\log_4 n)$, where $n$ is `n`. The space complexity is $O(1)$.  
The follow-up question could possibly be answered by exploiting the fact that the binary representation of powers of 4 follow an easily predictable pattern(only a single odd digit is raised).  
  

