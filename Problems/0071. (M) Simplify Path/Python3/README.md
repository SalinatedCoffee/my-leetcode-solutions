## 71. (M) Simplify Path

### `solution.py`
Retrieving a list of directory names from the given path is easy, as most languages support some form of string operation that splits the string based on some delimiter. We can iterate through this list discarding empty strings and single periods, and we would need to remove the most recent directory whenever a double period is encountered. A single `..` moves up one directory, but there may be consecutive occurrences of `..` which means we would need to keep track of all of the valid directories, in the order that they were processed. A stack is perfect for this situation as it provides constant time access to the most recent valid directory and preserves the insertion order of elements.  
Thus we iterate over the list of split tokens while pushing valid directories into a stack (`dirs`) and popping an item off the stack whenever a `..` is encoutered. Once the iteration has finished, the absolute path can be trivially reconstructed by appending popped directories from `dirs` in reverse order.  

#### Conclusion
The time and space complexity is $O(n)$, where $n$ is the length of `path`. `split()` takes $O(n)$ time, and in the worst case where `path` only has one directory `dirs` will contain a single string of length `n-1`.  
  

