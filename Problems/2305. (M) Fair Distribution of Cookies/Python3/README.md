## 2305. (M) Fair Distribution of Cookies

### `solution.py`
There seems to be no obvious way that we can divide this problem into smaller subproblems, so we know that a dynamic programming approach will most likely not work (or not be trivial). If anything, the constraints on the size of `cookies` being tiny gives us a clue as to how we should be tackling this problem. We can simply try all possible cookie allocations and return the minimum unfairness. One optimization we can make here is to back out of the recursion early when we have less jars of cookies than the number of children with no cookies at all. This is because we must hand out **all** jars of cookies in `cookies`, and so it is always optimal to give a child at least one jar.  
We will 'iterate' over `cookies` while trying to give the `i`th jar to each child and then recursing on the `i+1`th jar to see what happens. There are two base cases; when we have less jars left than the number of children with no cookies, and when all jars have been distributed. For the former, we simply return. For the latter, we return the largest number of cookies among the children. The initial call to this recursive function will be `recurse(0, k)`, as this represents the state where we are considering the `0`th cookie jar where all children have zero cookies.  

#### Conclusion
This solution has a time complexity of $O(k^n)$ where $k$ is `k` and $n$ is the length of `cookies`. Each recursive call performs `k` more recursive calls, and the height of the recursion tree is $n$, hence the overall time complexity of $O(k^n)$. The space complexity is $O(n)$, since the recursion stack will be $O(n)$ deep. `counts` is $k$ long, but $k \leq n$, per the input constraints.  
  

