## 1857. (H) Largest Color Value in a Directed Graph

### `solution.py`
Since the graph is directed, we need to traverse all paths starting at each node in order to count the occurrences of colors. We also need to traverse the graph in such a way so that we can detect cycles. Here we will be using recursive DFS, since cycles can be easily detected (when a traversed node has already been traversed). The color values of previously traversed paths should be kept track of, which we will do with a 2D list `count` where `count[i][c]` will contain the largest color value for color `c` among all paths that starts from node `i`. During traversal we return the memoized color value if the current node has already been visited, or we recurse on the node's neighboring nodes after which we also update the memoized color value for the current node, for all 26 colors.  
We now only need to run the traversal starting at each node in the given graph, and return the maximum value.  

#### Conclusion
This solution has a running time of $O(m+n)$ where $m$ is the length of `edges` and $n$ is the length of `colors` (number of nodes in the graph). The space complexity is also $O(m+n)$.  
  

