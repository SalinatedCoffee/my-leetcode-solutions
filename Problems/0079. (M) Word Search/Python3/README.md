## 79. (M) Word Search

### `solution.py`
We can immediately see that we could use recursion to traverse `board` while matching characters against the string `word`. Since we are not allowed to reuse characters, we must also keep track of all of the visited cells up to this point(essentially turning the problem into a DFS search).  
The function `recurse` takes 3 parameters; the row and column number of the current cell, and the index of the character in `word` that needs to be matched next. If the index is equal to the length of `word`, `word` exists in `board`, and we return `True`. Otherwise, we add the current cell to the visited set, and recurse down its neighbors if necessary. Because we only need to verify whether `word` exists in `board` or not, we can immediately return `True` the moment `word` is found in `board`.  

#### Conclusion
This solution has a time complexity of $O(mn3^k)$ where $m$ and $n$ are the dimensions of `board` and $k$ is the length of `word`. The DFS traversal can start at any cell of `board`(of which there are $mn$ of), and at each recursive step(of which there can be at most $k$ of) there are at most 3 cells that can be recursed on. The space complexity is $O(k)$, due to the visited set and the recursion stack.  
The follow up question asks us whether a faster solution can be implemented by implementing some sort of search pruning. This is a very general question in which the answer to can change drastically depending on what you expect from the input. For example, a frequency list of unique characters can be generated for both `board` and `word` to determine whether `word` can even exist in `board` before searching. However if the input statistically skews more towards `word` existing in `board`, and `board` being large compared to `word`, the overhead from this optimization will end up tanking the overall performance.  

