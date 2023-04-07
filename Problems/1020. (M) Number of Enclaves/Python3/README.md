## 1020. (M) Number of Enclaves

### `solution.py`
This problem is the exact opposite of [problem #1254](../../1254.%20(M)%20Number%20of%20Closed%20Islands/Python3), except we now want the total size of the connected components instead of the number of components. We can use DFS to traverse the traversed components and return the size of the component if none of the nodes are on the border.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $m$ and $n$ are the dimensions of `grid`. DFS can traverse every square in `grid` once, and `grid` is iterated over to determine whether a traversal should be initiated from a square. The space complexity is also $O(mn)$ since `visited` can contain all squares from `grid`.  
  

