## 43. (M) Multiply Strings

### `solution.py`
There are multiple ways of solving this problem, but here we have chosen to use long multiplication. We manually convert one string into an integer, and compute the product between it and the second string digit by digit. Once the computation is complete, we must convert that value back into a string, which can be easily achieved with a simple while loop.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the lengths of `num1` and `num2`, respectively. Converting each string is a linear time operation, and both strings are converted exactly once. The space complexity is also $O(m+n)$ since we construct the reversed string of the product before returning a string with the correct order.  
  

