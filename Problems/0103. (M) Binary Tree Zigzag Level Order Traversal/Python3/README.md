## 103. (M) Binary Tree Zigzag Level Order Traversal

### `solution.py`
This problem is a spin on [problem #102, Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/). We first need to figure out how to 'visit' the nodes in reverse order. Obviously we can't simply change the order of subtree appends as that would cause problems for any depth deeper than 2(assuming the root is at depth 1). The trick is to realize that it's much more easier to traverse the tree normally and *then* enumerate the nodes in the correct order rather than the other way around. So we can use standard BFS to traverse the tree level-by-level, in left-to-right order. A second queue is maintained which contains the values of the nodes at the currently traversed depth. Whenever a depth change is detected the contents of the per-level queue is appended to the result list in the appropriate order and `l2r` is flipped since we want to move in the opposite direction for the next level.  
Upon exiting the loop, we need to remember to check the per-level queue one more time since the nodes at maximum depth does not trigger a depth change.  
  
#### Conclusion
This solution takes $O(n)$ time to run where $n$ is the number of nodes in the tree. BFS visits each node exactly once, and operations on the per-level queue all take $O(1)$ time to run since we use a `deque` instead of a list. The space complexity is $O(n)$ since BFS traversals on a tree uses $O(n)$ space and `ret` will contain values for every node in the tree.  
  

