## 1218. (M) Longest Arithmetic Subsequence of Given Difference

### `solution.py`
This problem can clearly be divided into smaller subproblems with clearly defined state transitions between them. If we assume we know the longest subsequence length for the prefix array `arr[:i]`, we know that the longest length for the subarray `arr[:i+1]` will be that value incremented by `1`. However this is only the case when the value `arr[i]` is indeed the next value in the longest arithmetic subsequence in `arr[:i]`. We can trivially solve this using a dictionary (which we will call `dp`), where the key is a value in `arr` and the value is the length of the arithmetic subsequence that ends with that value. Thus while iterating through `arr` with loop variable `i`, the contents of `dp` will contain the lengths of the subsequences in the region `arr[:i]`.  
For each value of `arr` then, we check whether the previous value in the subsequence actually exists or not by looking for the key `arr[i] - difference` in `dp`. If it exists, we know that we can 'append' `arr[i]` to the end of that subsequence so the value of `dp[arr[i]]` becomes `dp[arr[i] - difference] + 1`. If not, a single value is considered to be a valid subsequence and so we set `dp[arr[i]]` as `1`. Note that this will still work when dealing with multiple elements of the same value because we would essentially be 'swapping' the tail element in the subsequence with a different element(eg. `arr = [1, 2, 3, 3, 3]`, `difference = 1`).  
Once the iteration has completed, we can simply look through all values in `dp` and return the largest one.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `arr`. `arr` is iterated over once, and during each iteration we only perform a fixed number of operations. The space complexity is also $O(n)$, since `dp` can at most contain $n$ key-value pairs.  
  

