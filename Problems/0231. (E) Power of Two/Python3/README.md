## 231. (E) Power of Two

### `solution.py`
For `n` to be a power of 2, it is not possible for it to be smaller than or equal to 0 for obvious reasons. Once `n` has been verified to be a positive value, we simply check whether the binary representation of `n` has a **single** raised bit. To do this, we can utilize a single while loop to shift `n` 1 bit towards the right until a raised bit is detected. If `n` is indeed a power of 2, `n` should be 0 after it is shifted by 1 bit.  

#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is `n`. Every time `n` is bit shifted, it is essentially halved. As the worst case is when `n` is indeed a power of 2, where it will be shifted all the way up to the MSB, the while loop takes $O(\log n)$ to run. The space complexity is $O(1)$.  
  


### `solution_2.py`
The follow up asks us to implement a solution without using loops of any kind(which also implies that `int.bit_count()` is not allowed). We can achieve this by exploiting how subtraction works. As established in the previous solution, the binary representation of a value that is a power of 2 only has 1 raised bit. If we were to subtract 1 from such a number, we would essentially be left with the complement of the original value. For example, the binary representation of 8 is `1000`. The value of 8 - 1 is 7, and *its* binary representation is `111`(a similar situation in base 10 would be subtracting 1 from 1000 to get 999). If we bitwise AND these two values, we would get `0`. Thus we can argue that if the expression `n & (n - 1)` evaluates to `0`, `n` is guaranteed to be a power of 2. The expression falls apart whenever `n` is not positive, so we must also remember to evaluate `n > 0` before evaluating the expression described above.  

#### Conclusion
The time and space complexity of this solution are both $O(1)$, assuming that integer subtraction takes constant time to compute(which we usually do since it is implemented in hardware, making it extremely fast).  
  

