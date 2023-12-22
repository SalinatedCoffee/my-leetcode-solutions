## 1422. (E) Maximum Score After Splitting a String

### `solution.py`
The trivial solution is to take the brute force approach and count the 0s and 1s for every possible split of `s`. As we will be examining every character in `s` for all `len(s) - 1` splits, the time complexity of this approach will be $O(n^2)$. We can do better by using some extra memory. If we think about the previously proposed solution, we can see that the characters in `s` will be counted multiple times. Instead, we can simply keep the character counts in memory to avoid redundant operations. We initialize a list `zeros` with length `len(s)`. `zeros[i]` will contain the number of `0`s in `s` to the left of `s[i]` inclusive. Once `zeros` is populated, we iterate over `s` in reverse while counting the number of `1`s to the right of the current element. During this iteration, we know the number of `0`s to the left of the current element `i` (`zeros[i-1]`) as well as the number of `1`s to the right, which is all of the information we need. We compute the score for each element and return the largest.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `s`. Initializing `zeros`, populating it, and computing scores while counting `1`s each take $O(n)$ time to complete. The space complexity is $O(n)$, as `zeros` has a length of $n$.  
  

