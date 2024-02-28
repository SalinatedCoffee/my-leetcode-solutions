## 513. (M) Find Bottom Left Tree Value

### `solution.py`
Essentially, the problem is asking us to find the left-most node in the last row of the given tree. There are many ways of solving this problem, but the most straightforward method is to use BFS to traverse the tree in level-order. We use a queue to store nodes to be traversed, along with their height. If we enqueue the left child of a node first, we can 'iterate' over the nodes in a level from left to right, which is what we want. Whenever a node popped from a queue has a different height from the previous node, it means that we have moved on to the next 'row' in the tree, and the current node is the left-most node within that row.  
Note that we do not know the height of the given tree, so the algorithm must be run to completeness.  

#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. Each node is visited exactly once, where each node takes constant time to process. `queue` can contain $O(n)$ nodes, hence its space complexity.  
  

