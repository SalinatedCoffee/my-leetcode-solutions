## 2696. (E) Minimum String Length After Removing Substrings

### `solution.py`
Given the string `s` which contains only uppercase English letters, we are asked to return the length of the shortest string that can be achieved by removing the substrings `"AB"` and `"CD"` from `s`. One thing to note is that the remainder of `s` should be concatenated after a substring is removed. For example, `s = "ZZZZACDBZZZZ"` would turn into `"ZZZZABZZZZ"` after removing `"CD"` from the original `s`, after which `"AB"` can be removed from the remaining string resulting in a final length of `8`.  
Immediately, we realize that the substrings are of length 2, which allows us to think of them as parentheses. If we iterate over `s` while keeping the current remaining characters in a stack, we can look at the top-most element on the stack and the current character of `s` to determine whether they can be removed. Otherwise, we push the current character onto the stack and move on until we finish iterating over `s`. Once the traversal completes, the number of elements in the stack is the number of characters in the remaining string, which we can directly return.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `s`. `s` is iterated over exactly once, with each character taking $O(1)$ time to process. The space complexity is also $O(n)$, due to the stack.  
  

