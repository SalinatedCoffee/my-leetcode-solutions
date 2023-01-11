## 908. (H) Unique Paths III

### `solution.py`

Intuition tells us that this problem can be solved with backtracking and DFS. Since all valid paths need to traverse all traversable squares once and only once, the given grid can be reused to mark squares we have already traversed (`3` in this solution). The initial solution is recursive with base cases of the given square being untraversable (out-of-bounds, obstacle, starting square, ending square but untraversed squares remaining) or the given square is the last step of a valid path (upon which the path is appended to the valid paths list). If the given position is traversable, it will mark the square accordingly and recurse on the neighboring 4 squares.

The return value of `len(ret)` is the result of me being an idiot and not reading the problem carefully.

#### Conclusion

The time complexity of the solution is $O(4^{mn})$, since it tries all four adjacent squares (even non-existent ones) for all squares on the grid. Not great, but works in this case because the grid size is very small.

Also, *always pay attention to solution specs.*

