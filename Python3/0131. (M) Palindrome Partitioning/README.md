## 131. (M) Palindrome Partitioning

### `solution.py`
By intuition, we know that we want to use backtracking for this problem since when a single substring is not a palindrome then any partition that include that substring is not valid. We can recursively 'iterate' over the string exiting early whenever we encounter a substring that is not palindromic.  
Implementing this in code is relatively simple - the base case for the recursive function is whenever the given indicies are outside of the range of the string, or when the substring `s[start:end+1]` is not a palindrome. For the former, we also check if `start` also oversteps the index range since that would mean that all previous substrings have been verified as palindromic. In the recursive case, we simply recurse on all other substrings with range starting from `end + 1`.  

#### Conclusion
The worst-case scenario is whenever the algorithm is given a string comprised of the same letter, in which case the time complexity is $)(n * 2^n)$ and the space complexity $O(n)$(excluding the return object).  
It takes $O(n)$ time to verify a substring and in the worst case there are $2^n$ possible partitionings, hence the overal running time of $O(n * 2^n)$. The recursive function can be thought of as a DFS traversal of a tree, from which we can see that the maximum depth is $n$(when the string is partitioned into single characters).  
  
### `solution_2.py`
We can further optimize the previous solution by realizing that it performs a lot of redundant operations. For example, given the string `aababaa`, it will evaluate `bab` multiple times (`a, ababa, a`, `a, a, bab, aa`... etc). By memoizing whether a substring is palindromic, we may avoid unnecessary computation. Before recursing on the string we set up a $n * n$ 2D list `dp` where `dp[start][end]` is `True` if the substring `s[start][end+1]` is palindromic, and vice versa.  
A substring is palindromic if the characters at the beginning and end of the substring is equal, and if either the inner substring has a length of 1 or less, or if `dp[start+1][end-1]` is `True`. If this check is passed we can update `dp[start][end]`.  

#### Conclusion
Since we do not explicitly validate all substrings, the time complexity is $O(2^n)$. The space complexity is $O(n^2 + n) = O(n^2)$ since `dp` has a size of `n * n`.  
  

