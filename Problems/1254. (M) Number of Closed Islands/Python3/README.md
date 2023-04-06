## 1254. (M) Number of Closed Islands

### `solution.py`
Essentially, we need to return the number of connected components that do not touch the grid's borders. This is trivially solved by performing a graph traversal for cells that contain `0` and checking whether the grid borders have been touched upon exiting the traversal. For this solution, we have implemented the iterative version of DFS. Whenever a border land square has been touched we flip the value of `border` and continue traversing. When the traversal has completed we check the value of `border` and return `False` if it is not `0`.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `grid`. DFS only traverses each land square once, and we iterate over the entirety of `grid` to see whether `dfs()` should be called on a square. The space complexity is also $O(mn)$ as `visited` can contain $mn$ elements in the worst case.  
  

