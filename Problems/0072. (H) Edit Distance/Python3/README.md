## 72. (H) Edit Distance

### `solution.py`
The [Edit Distance](https://en.wikipedia.org/wiki/Edit_distance) is a classic dynamic programming problem in computer science. The implementation is straightforward to understand and the problem itself has various practical applications such as autocorrect.  
But suppose this is the first time that we've encoutered this problem. How do we reason about it? Well, we know that a brute force approach wouldn't work as the time complexity would be exponential ($O(3^{m+n})$) since there are 3 choices we can make for every character in both words. Instead, we can set up a recursive relation that relies on precomputed values to make a decision. If we have prefixes for both words and want to decide what to do in order to match the next letter in the target word, we can do four things. The last letter in the source prefix and the next letter are the same and so we do nothing. Or they are different, and we can either add, remove, or replace the last letter to match the next letter. Let's examine the four choices we can make on prefixes `s_pre` (source prefix) and `t_pre` (target prefix).  
If we do nothing, the edit distance between `s_pre` and `t_pre` + `t_word[len(t_pre)]` is just the edit distance between `s_pre[:len(s_pre)-1]` and `t_pre`.  
If we add a letter to `s_pre` then the distance is the distance between `s_pre` and `t_pre` + 1.  
If we remove the last letter in `s_pre` then the distance is the distance between `s_pre[:len(s_pre)-1]` and `t_pre`.
If we replace the last letter in `s_pre` then the distance is the distance between `s_pre[:len(s_pre)-1]` and `t_pre` + 1.
If the characters are the same we can only do nothing, but if they are different we have 3 operations to choose from. In this problem we want to minimize the edit distance so the optimal choice is to select the operation that would result in the smallest distance.  
The base case is when either prefix is empty, at which point we can only either add or delete a character from the non-empty prefix. We can memoize these values in a 2D list `dp`, and incrementally fill it towards the bottom right where the desired value will be located.  
  
#### Conclusion
This solution has a time and space complexity of $O(mn)$ where $m$, $n$ are the length of strings `word1` and `word2`, respectively.  
Note that computing `dp[i][j]` only relies on 3 values, and the space complexity could be reduced to constant space. The trade off is that by doing this, we lose information about *how* a minimum distance edit could be performed between the two words.  
  
