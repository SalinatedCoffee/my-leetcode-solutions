## 108. (E) Convert Sorted Array to Binary Search Tree

### `solution.py`
Since the array is already sorted, a recursive solution is trivial. We simply split the array in half and recurse on the two halves. The base case is of course when there are no elements in the array that was recursed on.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the length of `nums`. The space complexity is $O(h) = O(\log n)$ as the recursion depth is the height of the tree being generated.  
  

