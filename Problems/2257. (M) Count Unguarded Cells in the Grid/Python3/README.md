## 2257. (M) Count Unguarded Cells in the Grid

### `solution.py`
A 2D grid contains walls and guards. A guard can guard all cells in their line of sight, in the same row and column the guard is positioned in. The line of sight is broken if there is a wall between a cell and a guard. For example, if a guard is positioned at `(1, 5)` and a wall exists at `(1, 3)`, the cells `(1, 0)`, `(1, 1)`, and `(1, 2)` will be unguarded. Given these conditions, the dimensions of the grid `m`, `n`,  the list of guards `guards` and list of walls `walls`, we are asked to determine the number of unguarded cells.  
One would be forgiven for initially gravitating towards graphs and attempting to come up with a 'clever' solution that tries to avoid marking each guarded cell. After considering a few options, we realize that they would all have the same time complexity as the brute force approach. We can simply initialize a 2D array that represents the grid, filling in the guarded cells after placing the walls and guards. The list of guards is iterated over, marking the cells in LOS of each guard. Note that we stop marking cells whenever we reach a wall *or* a guard, because we want to avoid marking cells that are destined to be marked in the future.  

#### Conclusion
This solution has a time complexity of $O(mn + k(m+n))$, where $m$ and $n$ are the values `m` and `n`, and $k$ is the length of `guards`. Initializing the grid, placing the walls and guards on said grid, and counting the number of unguarded cells each require $O(mn)$ time to complete. Marking all cells guarded by each guard takes $O(m+n)$ time to complete, since for a guard located at `(i, j)`, we would have to traverse the entire `i`th row and `j`th column in the worst case. The space complexity is $O(mn)$ since the $m\times n$ 2D array `grid` is kept in memory until the algorithm exits.  
  

