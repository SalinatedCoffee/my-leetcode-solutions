## 1249. (M) Minimum Remove to Make Valid Parentheses

### `solution.py`
A brute force solution would obviously not be feasible, as it would takes $O(2^n)$ time to run. As we want to construct a string by performing the minimum number of removals, we can greedily match open parentheses while iterating over `s`. In order to do this, we need to keep track of the number of currently open parentheses and the number of close parentheses in the untraversed portion of `s`. Using this information we can determine whether to include parentheses in the final string. If an open parenthesis is encountered, we should only include it if it can be closed in the future. We already know the number of unclosed parentheses up to this point, as well as the number of closed parentheses in the unexplored section of `s`. If the latter outnumbers the former, the current `(` can be closed in the future, so we include it in the string by pushing it onto the stack of included characters. If a close parenthesis is encountered, we can only include it if there are open parentheses available to be closed, which we can trivially check. Finally, if the current character is not a parenthesis, we do nothing and simply push it onto the stack.  
Once the entirety of `s` has been examined, the stack of characters can be concatenated as is to yield the desired string.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `s`. Populating the suffix count, the greedy step, and concatenation of the stack each take $O(n)$ time to perform. The space complexity is also $O(n)$, due to the stack and suffix counts being kept in memory.  
  

