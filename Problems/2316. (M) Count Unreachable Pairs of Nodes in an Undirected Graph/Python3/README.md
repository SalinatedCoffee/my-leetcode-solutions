## 2316. (M) Count Unreachable Pairs of Nodes in an Undirected Graph

### `solution.py`
If two nodes are not part of the same connected component, then they are obviously unreachable from each other. Conversely, if they are part of the same connected component then they are definitely reachable from each other. Identifying the individual components in the graph can be achieved in many ways, but for this solution we will utilize the iterative flavor of DFS.  
Once we have the list of the sizes of all of the disconnected components, we now need to compute the number of unreachable pairs in the entire graph. The brute force solution where we multiply the sizes for all pairs of components will take quadratic time and will fail with TLE upon submission. We can do better by realizing that we can compute the number of *every possible pairs* of nodes in the graph as we already know the size of the graph. This is simply $n\text{C}2 = n(n-1)/2$ as we are selecting 2 nodes in the graph. Then, we can iterate across the size of components and subtract the number of reachable pairs within the components from the total number of pairs computed earlier. Once the iteration has finished, we will be left with the number of unreachable pairs within the entire graph.  

#### Conclusion
The time complexity is $O(|V|) = O(n)$, where $n$ is the number of nodes in the graph. Determining the sizes of components takes $O(n)$ time (DFS) and computing the number of unreachable pairs of nodes in the graph also takes $O(n)$ time. The space complexity is $O(|V|+|E|)$ where $|E|$ is the number of edges in the graph, as the DFS step uses $O(|V|+|E|)$ memory.  
  

