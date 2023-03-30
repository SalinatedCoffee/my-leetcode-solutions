## 2360. (M) Longest Cycle in a Graph

### `solution.py`
Since each node can have at most only one outgoing edge, any given node can at most only be part of one cycle. Thus, we may simply attempt to traverse the graph starting at each node and record the size of the largest cycle. We need not traverse nodes that have already been visited as a node can only be part of one cycle. During the traversal, a cycle is detected whenever we encounter a node that has already been visited during the current traversal. If we maintain the distance from the source node to every traversed node it is trivial to compute the size of the cycle, which we compare against the currently largest cycle size.  

#### Conclusion
This solution has a running time of $O(n)$ where $n$ is the size of the graph since every node is traversed exactly once. The space complexity is also $O(n)$ as `visited` is the same length as `edges`, which is $n$ long.  
  

