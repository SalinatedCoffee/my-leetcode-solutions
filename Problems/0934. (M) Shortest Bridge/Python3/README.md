## 934. (M) Shortest Bridge

### `solution.py`

We can easily deduce that BFS can be used to determine the length of the shortest path between the two islands. The islands however, are comprised of multiple land squares which we must take into account. Thankfully the problem constraints state that there are only two islands on the grid, which in turn allows us to pick either island as the 'source' island. Thus, we may pick any land square on `grid` and identify the island that the square is a part of by using DFS (BFS would also work here). Once we have identified all of the land squares that is part of the island we may run BFS with all of the aforementioned squares as the source, and immediately return when the other island has been found.  



#### Conclusion

This solution has a time complexity of $O(n^2)$, where $n$ is the dimension of `grid`. DFS and BFS both have running times of $O(|V|)$, and for this problem $|V| = n^2$. The space complexity is also $O(n^2)$.  


