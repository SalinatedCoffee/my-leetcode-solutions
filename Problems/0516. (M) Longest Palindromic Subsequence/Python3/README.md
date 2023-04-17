## 516. (M) Longest Palindromic Subsequence

### `solution.py`
The brute-force method of considering every possible subsequence will take too long, as there are $2^n$ possible instances where $n$ is the length of `s`. Instead, we can try establishing a recursive relation and see where we can go from there. Say we have a function `lps(a, b)` that returns the length of the longest palindromic subsequence of string `s[a:b+1]`. We ultimately want the value of `lps(0,n-1)` where `n == len(s)`. What values, then, does `lps(0,n-1)` depend on? If `s[0] == s[n-1]`, then we can count the two letters at indices `0` and `n-1` and retrieve the length of the LPS starting at `0+1=1` and ending at `n-1-1=n-2`. This is simply `lps(1,n-2)+2`. If `s[0] != s[n-1]`, we can either advance the left index or retreat the second index. In the end we want the *longest* subsequence length, so we need to choose the larger value of the two. This is simply `max(lps(1,n-1), lps(0,n-2))`. The base cases are trivial, and we won't go into the details here.  
We have established the recursive relation but a naive implementation of the above will still take $O(2^n)$ time. Can we do any better? If we keep going down the recursion tree, we can see that there will be a lot of redundant computation that can be solved with memoization. Thus we instantiate a new 2D list `dp`, where `dp[i][j]` will contain the value of `lps(i,j)`. Then in `lps(a,b)`, we immediately return `dp[a][b]` if the value exists, or we make the necessary recursive calls as mentioned earlier.  

#### Conclusion
This solution has a running time of $O(n^2)$ where $n$ is the length of `s`. There are $O(n^2)$ number of ways that `lps()` can be called, and redundant calls will immediately return instead of proceeding down the recursion tree. The space complexity is also $O(n^2)$ since `dp` is an $n*n$ 2D list.  
  


### `solution_2.py`
The previous solution first made a call to `lps(0,n-1)`, which then worked itself *down* the recursive tree - a *top-down* dynamic programming approach. We may also come up with a *bottom-up* DP solution by considering the smallest sub-problems first and gradually building up to the desired problem. The recursive relationship and remembering-previously-computed-values strategy still stands, but this time we will compute the values for `dp` in the opposite direction. Again, we initialize a 2D list `dp` where `dp[i][j]` contains the value of `lps(i,j)`. We want the value that will be stored in `dp[0][n-1]`, so we start by computing the value of `dp[n-1][n-1]` and then fill in the values upwards, row-first. Notice that the values inside the triangular region of `dp` bound by indices `0,0`, `n-1,0`, and `n-1,n-1` will not be used as the substring represented by those indices will be invalid (or redundant, depending on how `lps()` is implemented. For example, what should `lps(2,7)` return?).  
We can easily implement this using nested loops, where the outer loop iterates over the rows of `dp` in reverse order and the inner loop iterates over the columns of the row from the outer loop. However, we can see that the computation of `dp[i][j]` only relies on values from `dp[i+1]` and `dp[i]`. Thus we may save on memory usage by only preserving the row from the previous iteration of the outer loop.  

#### Conclusion
The time complexity is $O(n^2)$ where $n$ is the length of `s`. The space complexity is $O(n)$, as we only keep two lists of length $n$.  
  
