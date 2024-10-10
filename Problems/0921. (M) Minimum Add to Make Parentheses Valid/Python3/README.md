## 921. (M) Minimum Add to Make Parentheses Valid

### `solution.py`
The string `s` consists of only the characters `(` and `)`. If in a single operation we can insert either one of these characters anywhere in `s`, we are asked to return the minimum number of inserts required to make `s` a balanced string. Because we can only balance one parenthesis per insert, we know that the answer is simply the total number of unbalanced parenthesis in `s`. We can count these characters by using a simulated stack, which is typical for problems involving balancing parentheses. A stack is simulated using two integers, since there is no need to store the actual characters in memory.  
Hanging open and close parentheses are kept track of by the integers `l` and `r`, respectively. We then iterate over each character of `s`, updating these integers as necessary depending on whether the character is an open or close parenthesis. For the former, we simply increment `l` by `1` as hanging close parentheses that occur earlier in `s` cannot be used to close the current open parenthesis. For the latter, we increment `r` by `1` if `l` is larger than `0`, which means that the current close parenthesis can be balanced by an unbalanced open parenthesis that occurs earlier in `s`. We reflect this balancing by also decrementing `l` by `1` if the current character has been balanced. Once the iteration completes we return the value of `l + r`, which is the total number of unbalanced parentheses present in `s`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. A single pass is made over `s`, with each character requiring $O(1)$ time to process. The space complexity is $O(1)$ since we use two characters that we use like a stack.  
  

