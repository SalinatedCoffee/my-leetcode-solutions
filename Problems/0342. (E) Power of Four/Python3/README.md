## 342. (E) Power of Four

### `solution.py`
For a number to be a power of 4, it cannot be negative or `0`, which we can trivially check before doing anything else. If `n` is positive, we simply continue dividing it by four while it is larger than `1`, and if at any point the remainder of the division is non-zero, we can immediately return `False`.  

#### Conclusion
This solution has a time complexity of $O(\log_4 n)$, where $n$ is `n`. The space complexity is $O(1)$.  
The follow-up question could possibly be answered by exploiting the fact that the binary representation of powers of 4 follow an easily predictable pattern(only a single odd digit is raised).  
  


### `solution_2.py`
Because 4 is itself a power of 2, we can easily rewrite the previous solution to use bit manipulation instead of division. We first recognize that the binary form of 4 is `100`, which means that if the 2 LSBs of a binary representation of a value are not `0`, that value could never be a multiple of 4. We also realize that since shifting a bitstring 1 digit to the right is equivalent to dividing that value by 2, we can shift a bitstring 2 digits to the right to divide the value by 4. Through these observations, we can define an algorithm as such:  

1. As long as `n` is greater than 1, repeat steps 2 and 3:  
2. Check the 2 LSBs of `n`; if they are not `0`, return `False`  
3. Shift `n` 2 binary digits to the right.  
4. If `n` is equal to 1, return `True`. Otherwise, return `False`.

The 2 LSBs of `n` can easily be examined by bitwise-ANDing it with 3.

#### Conclusion
The time and space complexity of this solution is identical to that of the previous; it will however, be faster in practice as it implements the same logic in a more efficient manner.  