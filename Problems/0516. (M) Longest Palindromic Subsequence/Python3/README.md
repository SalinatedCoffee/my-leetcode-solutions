## 516. (M) Longest Palindromic Subsequence

### `solution.py`
The brute-force method of considering every possible subsequence will take too long, as there are $2^n$ possible instances where $n$ is the length of `s`. Instead, we can try establishing a recursive relation and see where we can go from there. Say we have a function `lps(a, b)` that returns the length of the longest palindromic subsequence of string `s[a:b+1]`. We ultimately want the value of `lps(0,n-1)` where `n == len(s)`. What values, then, does `lps(0,n-1)` depend on? If `s[0] == s[n-1]`, then we can count the two letters at indices `0` and `n-1` and retrieve the length of the LPS starting at `0+1=1` and ending at `n-1-1=n-2`. This is simply `lps(1,n-2)+2`. If `s[0] != s[n-1]`, we can either advance the left index or retreat the second index. In the end we want the *longest* subsequence length, so we need to choose the larger value of the two. This is simply `max(lps(1,n-1), lps(0,n-2))`. The base cases are trivial, and we won't go into the details here.  
We have established the recursive relation but a naive implementation of the above will still take $O(2^n)$ time. Can we do any better? If we keep going down the recursion tree, we can see that there will be a lot of redundant computation that can be solved with memoization. Thus we instantiate a new 2D list `dp`, where `dp[i][j]` will contain the value of `lps(i,j)`. Then in `lps(a,b)`, we immediately return `dp[a][b]` if the value exists, or we make the necessary recursive calls as mentioned earlier.  

#### Conclusion
This solution has a running time of $O(n^2)$ where $n$ is the length of `s`. There are $O(n^2)$ number of ways that `lps()` can be called, and redundant calls will immediately return instead of proceeding down the recursion tree. The space complexity is also $O(n^2)$ since `dp` is an $n*n$ 2D list.  
  


### `solution_2.py`
The previous solution first made a call to `lps(0,n-1)`, which then worked itself *down* the recursive tree - a *top-down* dynamic programming approach. We may also come up with a *bottom-up* DP solution by considering the smallest sub-problems first and gradually building up to the desired problem. The recursive relationship and remembering-previously-computed-values strategy still stands. The difference here is that   

#### Conclusion
\<Content\>  
  
