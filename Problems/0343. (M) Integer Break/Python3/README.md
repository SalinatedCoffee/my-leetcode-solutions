## 343. (M) Integer Break

### `solution.py`
Intiution tells us that we can apply a dynamic programming based approach to this problem as the problem can clearly be broken down into smaller subproblems. For instance, if we know the max product of breaking down some integer `i` (where `i < n`) we could use that information to compute the max product of a larger integer.  
We can take a top-down approach here by realizing that the max product of some integer depends on the max products of all possible splits. That is, the max product of some integer `i` will be the largest value among `max_prod(i - s) * s` for all possible `s`, which is the split. Of course, another option would be to simply not split `i` at all. The base cases are when `i <= 3`. It is trivial to see why when `i == 1`, and when `i == 2` or `i == 3`, all possible splits would result in a value that is smaller than `i`, and thus it is optimal to not split `i`. One more thing to keep in mind that a given value must be split into *at least* 2 parts. This means that we need check whether `n <= 3` *before* entering the recursion, as the recursive function will not split any value that satisfies this requirement (the base cases).  
Defining a fuction `recurse(rem)`, which will return the max product of the integer `rem`, we first check the condition `rem <= 3`. If true, we simply return `rem`. Otherwise, we initialize `ret` to `rem` (the case where `rem` is not split at all) and try updating `ret` for all splits `s` in the range `2` to `rem`. Once all splits have been considered, we may then return `ret`.  
By definition, we want the return value of `recurse(n)`, which we call in `integerBreak` if `n` is larger than `3`. Otherwise, we return `n - 1`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is `n`. For some value $i$, all possible splits are considered, which there are $O(i)$ of. Since we want the max product of $n$, the overall time complexity is $O(n^2)$. The space complexity is $O(n)$, as there are $O(n)$ states that are kept in memory.  
  

### `solution_2.py`
There is also a mathematics-based approach that can be taken, which loosely relates to the base cases that were discussed in the previous solution. The key takeaway is that it is always optimal to split a number into as many `3`s as possible, and one or two `2`s depending on the number being split.  
The unformal proof starts with the [inequality of arithmetic and geometric means](https://en.wikipedia.org/wiki/AM-GM_Inequality), which states that a value should be split into equal parts in order to maximize their product. Splitting $n$ into $a$ identical pieces of $x$, we get that $n = ax$, or $a = n/x$. The product of these pieces will be $x^a$, and so we substitute $a$ and define a function $f$ with $x$ as its parameter. We now have $f(x) = x^{n/x}$, which we want to maximize. Taking the derivative of $f$ we get $f'(x) = -nx^{n/x-2}\cdot (\log x - 1)$. Examining the critical points of the function, we realize that $f$ is maximized when $x = e$. $e$ however, is not an integer, which means we need to round up to $3$.  
If the remainder of a number after splitting it into `3`s is `1`, it is clearly optimal to 'unsplit' 1 piece to make the remainder `4`, which can be split into 2 `2`s which has a larger product than `3` and `1`. The other case is when the remainder is `2`, which we can leave as is. According to this algorithm we can simply divide `n` by `3`, and determine the number of `2`s by looking at the remainder of the division. If the remainder is `1`, the split should include 2 pieces of `2`. If it is `0`, all pieces are `3`. Otherwise, the split should include only 1 piece of `2`.  

#### Conclusion
The time complexity of this solution is $O(\log n)$, or $O(1)$ depending on how exponentiation is implemented. The space complexity is $O(1)$.  
  

