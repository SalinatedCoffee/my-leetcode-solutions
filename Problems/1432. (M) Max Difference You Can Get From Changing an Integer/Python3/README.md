## 1432. (M) Max Difference You Can Get From Changing an Integer

### `solution.py`
We can apply a single operation on an integer that involves the following steps:  

 - Select any number `a` from `0` and `9` inclusive.
 - Select another number `b` from `0` and `9` inclusive(`a` and `b` are allowed to be equal).
 - Swap in `b` into all digits in the integer that are equal to `a`.
 - The resulting integer **must not** have any leading zeros, nor be equal to `0`.

For example, assume that we have the integer `5442`. If we were to select `5` as `a` and `3` as `b`, we would end up with the integer `3442`. Given the integer `num`, we are asked to determine the largest difference between two values resulting from the application of the described operation on `num`.  
First off, we would obviously want to determine the largest and smallest possible result. The former is rather trivial - we simply iterate over each digit of `num` in descending order of significance, and select the first value not equal to `9` as `a` and `9` as `b`. The latter is slightly more complicated as we are not allowed to have any leading zeroes after applying the operation. First of all, we know that the MSD(most significant digit) cannot be `0` since it is not possible for `num` to have leading zeros. We also know that we cannot change the MSD to `0` as we are not allowed to have leading zeros in the result after performing the operation on `num`. However, we would absolutely want to change the MSD to `1` if it is not already `1` to maximize the difference between `num` and the resulting number after the operation is applied to it. Otherwise, we examine digits in descending order of their significance and swap the first non-zero digit with `0`s. We can achieve this by simply iterating from the digits from left to the right, moving on to the next digit only if the digit is *less than or equal to `1`*. Whenever the current digit is greater than `1`, we break out of the loop and check the position of the digit. If it is the MSD, we simply swap all corresponding digits out with `1`. Otherwise, we swap the digits out with `0`.  
Once we have the maximum and minimum results, we can simply compute the difference and return it.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where `n` is `num`. Iterating over each digit of `num` is a $O(\log n)$-time operation since `num` has $\log n$ digits; hence the overall time complexity of $O(\log n)$. The space complexity is also $O(\log n)$, as we store the list of digits of `num` in memory.  
  

