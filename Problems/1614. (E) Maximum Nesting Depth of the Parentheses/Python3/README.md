## 1614. (E) Maximum Nesting Depth of the Parentheses

### `solution.py`
Because `s` is guaranteed to be a valid set of parentheses, we can easily solve this problem by emulating a stack. The counter `cur` is increased by `1` when an open parenthesis (`'('`) is found, and decreased by the same amount when a closed parenthesis (`')'`) is encontered. Whenever the counter is increased we update the maximum depth `ret` accordingly. Once the entirety of `s` has been examined, we can directly return `ret`, which will contain the maximum parenthesis depth.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. The string is iterated over once, and each character takes $O(1)$ time to process. The space complexity is $O(1)$ as we only make use of a handful of fixed-size variables.  
  

