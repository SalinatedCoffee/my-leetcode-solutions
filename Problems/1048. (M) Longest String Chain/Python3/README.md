## 1048. (M) Longest String Chain

### `solution.py`
We can intuitively say that we should be taking a dynamic programming approach to this problem, since the problem looks like in can be split into smaller subproblems. The obvious way of implementing this approach involves initializing an array `dp`, where `dp[i]` will contain the length of the longest string chain within the prefix subarray `words[:i]`. This however will not work, for a couple of reasons; first, when examining some word `i`, we will not know which word the LSC ends with. Second, even if we knew which word the LCS ends in, there may be multiple possible candidates that would lengthen the chain, but there is no way for us to determine which is the most optimal, and no way for us to simply try all possible words.  
The trick here is to move backwards - this way, the predecessor words that a word 'depends' on will already have been processed, allowing us to definitively choose the most optimal word.  
In order to ensure that we can check whether a word exists in `words` in optimal time, we create a dictionary `d_words` with each word as the key and the length of the LSC ending with that word as the value. We then sort `words` in ascending order of the word's length. Because a successor **must** include an extra character, we can say that if a word `A` is shorter than another word `B`, `A` can never be a successor of `B`. By sorting `words`, we can use this fact to make sure that the candidate predecessors are already processed. Then, for each word `word`, we try taking out a character and see if the new word actually exists in `words`. If so, we chain the words together only if the new chain results in a longer chain than we already have for `word`. Once we have finished processing every word we need to return the longest chain length among all words, which is simply the maximum value in the dictionary `d_words`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `words`. The sorting step takes $O(n\log n)$ time, and the chaining step takes $O(n)$ time. The chaining step iterates along `words` once and each word takes $O(16) = O(1)$ time to process, hence, the chaining step takes linear time to run and the overall time complexity is $O(n\log n)$. The space complexity is $O(n)$, as `d_words` will contain $n$ key-value pairs.  
  
