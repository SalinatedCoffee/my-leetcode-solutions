## 463. (E) Island Perimeter

### `solution.py`
One possible approach is to traverse the land cells using a graph traversal algorithm. As the island is traversed, we simply need to count the number of land cells and adjacencies to compute the perimeter of the landmass. Since it is guaranteed that `grid` only contains 1 landmass, we can arbitrarily select any land cell as the starting point. To avoid overcounting, all visited cells are stored in a set. For this approach, one detail that should not be overlooked is how the adjacent edges are counted. For example, if `grid = [[1, 1], [1, 1]]`, DFS will traverse the island in a 'snake-like' fashion. If we assume that it starts at `grid[0][0]` and examines its neighbors in the order of up, right, down, left, `grid` will be traversed in the order `grid[0][0]`, `grid[0][1]`, `grid[1][1]`, and `grid[1][0]`. At the last cell, the algorithm will attempt to move to `grid[0][0]` but will ignore it, seeing that it already has been visited. However, we still want to count the adjacent edges between the two cells. To solve this problem, we simply count the adjacent edges *before* moving to the cell(in other words, we increment the counter when the neighboring cell is pushed onto the stack). This way, in the previous example, the adjacent edge between `grid[0][0]` and `grid[1][0]` would have already be counted when visiting `grid[0][0]`.  
Once the traversal finishes, we simply multiply the number of land cells by 4, and subtract the number of adjacent edges multiplied by 2.

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `grid`. There can be at most $mn$ land cells, and since all land cells are visited exactly once, the island takes $O(mn)$ time to traverse via DFS. The space complexity is also $O(mn)$, due to how the cells are pushed onto the stack.  
  


### `solution_2.py`
There is yet another way that this problem can be solved, without using a graph traversal algorithm. As edges only exist between two different types of cells, we can simply iterate over `grid` while counting the number of changes between adjacent cells. `grid` is iterated over two times; once to count the number of vertical edges (horizontally adjacent cells) and once to count horizontal edges. This method also has the added bonus of working on cases where there are multiple islands, since it examines the entirety of `grid` without caring about adjacent land cells.  

#### Conclusion
The time complexity of this solution is $O(mn)$. The space complexity is $O(1)$.  
  

