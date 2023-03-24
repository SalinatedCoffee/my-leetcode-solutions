## 417. (M) Pacific Atlantic Water Flow

### `solution.py`
The simplest method would be to perform a graph traversal for every square and return the ones that reach both oceans. This however would result in a time complexity of $O(mn^2)$, where $m$ and $n$ are the dimensions of the grid. We can do better by reversing the source and destination and traversing the grid from the 'shore' squares instead. Then the visited set of nodes naturally becomes the set of nodes that can reach an ocean. If we keep two visited sets for each ocean, the intersection of these sets will contain the squares we want.  
Thus we start a graph traversal (in this case, DFS) on the 'shore' squares and return the intersection of the two 2D lists `p` and `a`.  

#### Conclusion
This solution has a running time of $O(mn)$, where $m$ and $n$ are the dimensions of `heights`. The grid is traversed once for each ocean, and the final intersection step also involves scanning a 2D list with the same dimensions as `heights`. The space complexity is also $O(mn)$.  
  

