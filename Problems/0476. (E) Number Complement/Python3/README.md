## 476. (E) Number Complement

### `solution.py`
Given the integer `num`, we are asked to return its binary complement as an integer. For example if `num = 11`, the returned value should be `4` since `11 = b1011` and the complement of `b1011` is `b0100`, which is `4` in base 10. Because we are working with only non-negative integers, we cannot use the `~` operator in Python to flip the bits of `num`. Instead, we must manually compute the complement of `num` by first converting it into binary in the form of a list of bits, and then generating the complement by iterating over said list.  

#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is `num`. $n$ in base 10 has $\log n$ digits in binary, which are iterated over with each digit taking constant time to process. The space complexity is also $O(\log n)$, since the list of binary digits `bits` are kept in memory.  
  


### `solution_2.py`
Instead of iterating over each binary digit of `num`, we can utilize the properties of the XOR operation to compute the binary complement more easily. XORing a bit with `1` has the same effect as flipping that bit, and as such, we can flip every bit in `num` by XORing it with a binary number with the same number of digits as `num` consisting of only `1`s. Returning to the example given in the previous solution `num = 11`, the XOR mask would be `b1111`, which when XORed with `11 = b1011` would yield a value of `b0100`, which is indeed the desired value. We first count the number of digits in the binary representation of `num`, after which we create the XOR mask by subtracting `1` from the value `2**m` where `m` is the number of binary digits in `num`.  

#### Conclusion
The time complexity of this solution is identical to the previous solution, but will run faster in practice. The space complexity is $O(1)$, since unlike the previous solution there is no need to keep the binary digits of `num` in memory.  
  

