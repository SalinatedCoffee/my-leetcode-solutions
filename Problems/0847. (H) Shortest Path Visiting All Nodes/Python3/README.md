## 847. (H) Shortest Path Visiting All Nodes

### `MLE.py`
We can use BFS to determine the shortest path, however we will need to keep track of which nodes have been previously visited in order to determine whether all nodes have been traversed. Since the given graph can at most contain 12 nodes per the problem constraints, we may represent the set of visited nodes as a bit string. If the `i`th digit (0-indexed) is `1`, it means that node `i` has been previously visited.  
The queue with nodes yet to be traversed is initialized with all nodes as the origin, with the corresponding bit set for their visited integers. Then we simply perform BFS, and return the distance whenever all nodes have been visited.  

#### Conclusion
This algorithm will fail with MLE because it will unnecessarily revisit previously traversed nodes. The time and space complexity is $O(n^n)$, where $n$ is the number of nodes in the graph represented by `graph`.  
  

### `solution.py`
The previous attempt can be modified to reduce the time and space complexity. The objective is to minimize the distance it takes to traverse all nodes. Hence if there are multiple ways of visiting some node `i` where `v` nodes have been visited, we would naturally want to continue exploring the path with the smallest distance. Our previous attempt exactly guarantees this by virtue of using BFS. As such, whenever the state where we are currently at some node having visited some other nodes have been observed before, we simply stop exploring any further.  
When all nodes have been visited, we may immediately return the distance traversed.  

#### Conclusion
This solution has a time and space complexity of $O(n2^n)$. We begin the BFS traversal with all nodes as the source, and for each source there can be $O(2^n)$ possible subsets of the given graph. `visited` stores states that have 2 parameters; one that is in the range $[1, 2^n]$ (set of visited nodes) and another in the range $[1, n]$ (the current node).  
Note the similarity between this solution and the [Floyd-Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm).  

