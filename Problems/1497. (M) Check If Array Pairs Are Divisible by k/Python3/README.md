## 1497. (M) Check If Array Pairs Are Divisible by k

### `solution.py`
Given the list of integers `arr`, we are asked to determine whether its elements can be paired such that the sum of each pair is divisible by `k`. For example, if `arr = [1, 2, 3, 4, 5, 6]` and `k = 7`, `True` should be returned as `arr` can be grouped into the pairs `(1, 6)`, `(2, 5)`, and `(3, 4)`.  
Because we are asked to pair elements such that the sum of each pair is *divisible* by `k`, we immediately gravitate towards modulo operations. If the integer `i` mod `k` results in the value `i_k`, we know that adding `i` to another integer `j` where `j % k` equals `k - i_k` will result in a value that is divisible by `k`. Thus, if the number of elements in `arr` where the value of modulo `k` is some integer `i` is `a`, we know that `arr` cannot possibly be paired if the number of elements where their value modulo `k` is `k - a` is not equal to `a`. One edge case that should be considered is when `a = 0`. In this case, `j % k` should also equal `0` for `i + j` to be divisible by `k`; that is, the number of elements in `arr` where their value modulo `k` equals `0` should be even. If any of these checks fail for `i` in the range `[0, k//2]`, we can definitively say that the elements of `arr` cannot be paired in accordance to the problem requirements.  
We keep track of the number of elements mod `k` using the Python `Counter` `freq`, which can be easily done with a single list comprehension. The edge case of `i = 0` is then checked by evaluating the expression `freq[0] % 2 != 0`. If it evaluates to `True`, we immediately return `False` as the elements in `arr` cannot be paired. Otherwise, we evaluate the validity of all remaining values of `i`. Iterating over each integer `i` in the range `[1, k//2+1)`, we simply check whether the expression `freq[i] != freq[k-i]` evaluates to `True`. If so, we return `False`. If the loop exits normally all elements in `arr` can be paired, and we return `True`.  
  

#### Conclusion
This solution has a time complexity of $O(n+k)$, where $n$ is the length of `arr` and $k$ is `k`. Instantiating a `Counter` using `arr` takes $O(n)$ time, and the evaluation step that follows requires $O(k)$ time to complete. The space complexity is $O(k)$, due to the `Counter` `freq`.  
  

