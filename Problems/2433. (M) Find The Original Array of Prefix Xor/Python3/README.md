## 2433. (M) Find The Original Array of Prefix Xor

### `solution.py`
We can use boolean algebra to solve this problem. One property of XOR operations is that the results of XORing a value with itself continuously flips between itself and `0`. For example, `5 ^ 5 = 0`, `5 ^ 5 ^ 5 = 5`, `5 ^ 5 ^ 5 ^ 5 = 5`, and so on. Another property that we can take advantage of later is that XORing a value with `0` always results in the non-zero value itself, which means that in the expression `5 ^ 0`, we can simply ignore the `0` and simplify it down to just `5`.  
Moving onto the first example, let's first start working through the first step, where we are asked to determine the integer `i` where `5 ^ i = 2`. Using the properties of XOR described above, we can XOR both sides with `5` to get `5 ^ 5 ^ i = 5 ^ 2` (XOR is also both associative *and* commutative). The `5 ^ 5` in the LHS results in `0`, which as we have established earlier can simply be ignored. Thus we are left with the equation `i = 5 ^ 2`, which is trivially solvable. As XOR is associative and commutative we can apply this method to all values of `pref`, computing the appropriate value of `arr` at each step.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `pref`. Bitwise operations are most often directly translatable to the underlying hardware, taking $O(1)$ time to compute. $n$ values are processed, where each computation only takes constant time. The space complexity is $O(1)$, excluding the return list `ret`.  
  

