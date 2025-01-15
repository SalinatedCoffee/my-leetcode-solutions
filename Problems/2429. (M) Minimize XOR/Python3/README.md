## 2429. (M) Minimize XOR

### `solution.py`
Given the positive integers `num1` and `num2`, we are asked to determine some positive integer `x` that satisfies the following conditions:  

- `x` has the same number of raised bits as `num2`.  
- The value of `x XOR num1` is minimal.  

Counting the number of raised bits in `num2` is trivial, and will allow us to meet the first condition. For the second condition, we can start by recalling that an XOR operation between bits `a` and `b` essentially flips `a` if `b` is `1`. That is, the resulting value will be `1` if `a` is `0`, and `0` if `a` is also `1`. Because we want to minimize the value of `x XOR num1`, we obviously want to prioritize the flipping of the leftmost raised bits. Starting with the most significant bit(MSB), we raise the same digit in `x` if the bit in `num1` is raised in that position. We continue to move towards the LSB as long as the number of raised bits is less than that of `num2`. If more bits have to be raised still after reaching the LSB, we make a second pass over `num1` in reverse. This time, we raise the corresponding bit in `x` if the current digit of `num1` is `0`. As we cannot 'unraise' a set bit in `x`, we must raise unraised bits in ascending order of their significance. We continue setting bits until we number of bits raised becomes equal to that of `num2`.  

#### Conclusion
This solution has a time complexity of $O(\log m + \log n)$ where $m$ and $n$ are `num1` and `num2`, respectively. Counting the number of raised bits in `num2` takes $O(\log n)$ time, as `num2` is essentially halved every time it is shifted 1 bit towards the right. Similarly, iterating through each binary digit of `num1` requires $O(\log m)$ time to complete, with each digit taking $O(1)$ time to process. The space complexity is $O(1)$.  
  

