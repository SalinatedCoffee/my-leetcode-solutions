##547 (M) Number of Provinces

### `solution.py`
This problem ultimately boils down to finding the number of connected components. Since the input graph is given to us as an adjacency list we can use `isConnected` directly without having to generate one of our own. We try traversing the graph (iterative DFS is used here, but other traversals will also work) starting at each node and increment a counter whenever a source node has not been visited (indicating that the component that the source node is part of has not been counted yet).  

#### Conclusion
The time complexity of this problem is $O(n)$, where $n$ is the number of cities(the length of `isConnected`). Each node is visited exactly once since `visited` is shared across all traversals. The space complexity is also $O(n)$, since the size of `visited` is $O(n)$.  
  

