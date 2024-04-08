## 678. (M) Valid Parenthesis String

### `solution.py`
We can immediately see that this problem can be solved by using recursion, as we can divide the problem into smaller subproblems. At each recursive call, we will need 2 pieces of information to determine which action to take; the position within `s` currently being considered, and the number of unclosed open parentheses previously encountered. Because we may call this function with the same parameters multiple times (for example, if `s = "(*(*"`, the first `*` can be interpreted as the empty string and the second as `(`, and vice versa) we can also memoize intermediate results to prevent redundant computation.  
The function `recurse` takes 2 arguments. `o` is the number of previously encountered unclosed open parentheses, and `i` is the position within `s` that is currently being considered. If `i == len(s)`, we have reached the end of `s`, and so we return `True` if there are no open parentheses (`o == 0`) or `False` otherwise. If this is not the case, we look at `s[i]` to determine our next course of action. If it is `(`, we simply perform a recursive call after incrementing `o` and `i` by `1`. If it is `)`, we recurse only if there are open parentheses that can be closed (`o != 0`). If it is `*`, we try interpreting it as `(`, `)`, or the empty string. Since we are only interested if there are *any* possible interpretations that makes `s` valid, we can immediately return `True` whenever a recursive call also returns `True`. Otherwise, we simply return `False`.  
By definition of `recurse`, the value we want is the return value of `recurse(0, 0)`, which we can directly return.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the length of `s`. Our recursive function has 2 parameters `o` and `i`, both of which are bound by $n$. Since computing each recursive call takes constant time, and there are $O(n^2)$ states that requires evaluation, the overall time complexity is $O(n^2)$. The space complexity is also $O(n^2)$, as we memoize every intermediate result.  
  

