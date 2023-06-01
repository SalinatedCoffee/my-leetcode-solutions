## 1091. (M) Shortest Path in Binary Matrix

### `solution.py`

Dynamic progamming will not work here since a path could include an interval that moves *away* from the goal - there is nothing to optimize. Instead, we can use BFS to traverse the grid and return immediately when the goal has been reached. One optimization we can make is to check whether a square was visited right before it is pushed to the node queue, and marking it as such immediately after. This way, we can avoid reprocessing the same node multiple times.  

A valid path does not exist when the source node $(0,0)$ is a 1-square or when the BFS loop exits normally.  

#### Conclusion

The time and space complexity of this solution is $O(n^2)$, where $n$ is size of `grid` on one side. BFS processes all valid nodes exactly once, and at each node there are a fixed number of neighboring nodes to consider. `visited` contains $n^2$ elements, and `nodes` will use $O(n^2)$ memory.  


