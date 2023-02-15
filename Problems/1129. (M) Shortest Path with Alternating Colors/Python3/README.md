## 1129. (M) Shortest Path with Alternating Colors

### `solution.py`
By intuition, BFS seems like a good approach for this problem as it asks us to compute the lengths of the shortest paths to all nodes. The problem now then becomes how we should handle traversing the colored paths. This is where LeetCode gets a bit sloppy - it talks about paths, which by definition means that nodes can be visited only once. However one of the test cases *does* involve reaching a node through a path with a cycle. This has to do with how we actually perform BFS which we will get to later. Returning to the problem, we know that we can take all outgoing blue edges if we reached that node via a red edge, and vice versa. So what if we 'split' a node in two, one that represents reaching that node through a red edge and another for a blue edge? Now we can run vanilla BFS on this graph, alternating between edges of the two colors. The confusing problem description mentioned earlier makes sense here, where we consider a node as two separate nodes based on the color of the previously taken edge.  
In terms of actual implementation we need to remember to add *all* outgoing edges from node `0` initially since we just start at it instead of taking an edge from some other node.  

#### Conclusion
This problem takes $O(n)$ time and space where $n$ is the number of nodes in the graph. The new graph takes $O(2n) = O(n)$ time to traverse, and `adj`, `visited` both uses $O(n)$ memory.  
The 'split node' strategy is given as a hint, so I suspect whoever wrote the description just assumed that people would read it. It's not a big deal, but still quite annoying.  
  
