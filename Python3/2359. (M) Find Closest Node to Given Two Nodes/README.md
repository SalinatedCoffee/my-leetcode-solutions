## 2359. (M) Find Closest Node to Given Two Nodes

### `solution.py`
This is a weird one, I'm not going to lie. But despite its weirdness it's rather easy to solve. Since a node has at most only one outgoing edge (so a graph with `n` nodes can have at most `n` edges), we can simply use BFS to generate a dictionary with the node labels as keys and the path length as values. Then, we just iterate through all nodes while updating the minimum length of `max(n1, n2)` where `n1` and `n2` are the length of the shortest paths to the current node from `node1` and `node2` respectively.  

#### Conclusion
The solution has time and space complexities of $O(n)$.  
  

