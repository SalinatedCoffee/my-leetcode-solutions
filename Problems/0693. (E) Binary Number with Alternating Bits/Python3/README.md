## 693. (E) Binary Number with Alternating Bits

### `solution.py`
Given the positive integer `n`, we are asked to determine whether its binary representation is comprised wholly of alternating bits, returning `True` if yes and `False` otherwise.  
We can trivially solve this problem through the use of a handful of bitwise operations. The main idea is that when given any bit at any location within the binary representation of `n`, we already know what its neighboring bits should be for `n` to be only comprised of alternating bits. We will store this 'should-be' bit in the variable `exp`, initializing it as the LSB of `n`. Then, starting at the LSB of `n`, we iteratively examine each binary bit of `n` from right to left. A bit is first compared against the expected bit `exp` to check that it is indeed alternating. If they are not equal, we may immediately return `False`. If the comparison succeeds, we flip `exp` before shifting `n` 1 bit to the right. We repeat these steps until all bits of `n` have been examined (`n == 0`), which means that all bits of `n` are indeed alternating, and we can return `True`.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where $n$ is `n`. `n` is shifted 1 bit to the right until it becomes `0`. `n` has $\log n$ binary digits; and since each digit requires $O(1)$ time to process, the overall runtime of this solution becomes $O(\log n)$. The space complexity is $O(1)$.  
  

