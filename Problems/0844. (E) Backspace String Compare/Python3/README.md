## 844. (E) Backspace String Compare

### `solution.py`
It should be immediately apparent that we can use stacks to trivially solve this problem. As we examine each character in `s` and `t` in order, we push it on to the stack if the character is not `'#'`. If it is, we pop an element off the top of the stack, if it exists. Once the entire string has been examined, we simply concatenate the contents of the stack back into a string, which is the string after the backspaces have been processed.  
After converting both strings `s` and `t`, we simply do a linear comparison between the processed strings and return `True` if they are an exact match.  

#### Conclusion
This solution takes $O(m+n)$ time to run, where $m$ and $n$ are the lengths of strings `s` and `t`, respectively. Processing each string takes linear time, as well as the comparison step between the two processed strings. The comparison however is bound by $\text{max}(m, n)$, putting the overall time complexity at $O(m+n)$. The space complexity is also $O(m+n)$, as we keep both processed strings in memory in order to compare them.  
  

