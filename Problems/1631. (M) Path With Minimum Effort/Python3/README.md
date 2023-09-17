## 1631. (M) Path With Minimum Effort

### `solution.py`
Because we want a path from a source to a destination while optimizing some value, we should be using Dijkstra's algorithm in solving this problem. Dijkstra's algorithm is typically used to find the path with the smallest total weight given a graph with positive weights. For this problem we need to modify this algorithm slightly as we want the path with minimum effort.  
The setup is similar to the original version of Dijkstra's algorithm. We initialize a distance matrix `dist`, where all efforts are initialized as `10**6` except the source cell, which is initialized to `0` instead. A min-heap is used to store nodes to be processed, and is ordered by the effort required to reach that node. Until the destination cell is reached, we pop the cell with the smallest effort from the heap and explore its neighbors. A neighbor however, is only worth exploring when the effort required to reach it is smaller than its current smallest effort on record. The effort required to move between cells is defined as the absolute difference between their values in `heights`. Since we want to *minimize* the *maximum effort* of a path, we need to update the new path effort accordingly by moving to a cell's neighbor. This new effort is simply either the effort it took to reach the current cell, or the effort required to move to the neighboring cell, whichever is larger.  
When the destination is reached, we may immediately return the effort of the destination as the algorithm guarantees that the first visit to the destination will always have the smallest effort.  

#### Conclusion
This solution has a time complexity of $O(mn\log mn)$, where $m$ and $n$ are the dimensions of `heights`. Dijkstra's algorithm can at most traverse all cells of `heights`, and for each traversal at least 1 heap operation is performed, which can take $O(\log mn)$. The space complexity is $O(mn)$ since we store the effort of each cell in `dist`, which is an $m\times n$ 2D list.  
  

