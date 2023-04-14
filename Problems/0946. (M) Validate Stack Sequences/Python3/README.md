## 946. (M) Validate Stack Sequences

### `solution.py`
The necessity of a stack for this problem is quite obvious, the main problem is figuring out how to determine whether the two given list of numbers are valid. This is thankfully rather straightforward as well, since we cannot pop from the stack if the current operation in `popped` does not match the value on the top of the stack. Thus we iterate over `pushed`, pushing the current element into a stack. We also maintain a pointer in `popped` which points to the next element that would be popped from the stack. After the push we compare the top of the stack and the value in `popped` currently pointed to, and keep popping from the stack until the two values do not match.  
Once we are done iterating over `pushed`, we can return `True` if the pointer to `popped` is pointing to index `len(popped)` as that would mean that all elements in `popped` have been successfully removed. The stack does not need to be empty after all operations have been performed, so we do not need to check whether `stack` is empty.  

#### Conclusion
This solution runs in $O(n)$ time and space, where $n$ is the length of `pushed`. All elements in `pushed` are pushed onto `stack` exactly once, which takes $O(1)$ time each. At worst, `stack` can contain all elements of `pushed` when the first element of `popped` is not in `pushed` - hence the space complexity of $O(n)$,  
  

