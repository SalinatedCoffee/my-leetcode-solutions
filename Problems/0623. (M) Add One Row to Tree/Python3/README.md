## 623. (M) Add One Row to Tree

### `solution.py`
This is a problem that can be solved fairly trivially as long as we handle the linking of existing nodes properly. As we want to create new nodes at a certain depth we should traverse the tree with BFS as it performs a level-ordered traversal. In this solution we have opted to implement the iterative flavor of BFS, using a Python deque to enqueue the nodes of the tree. When enqueueing a node we also need to bundle the depth with it, as a `TreeNode` object by itself does not contain any information about its depth within the tree. While the tree is traversed, we first check the depth of the current node being examined. If it is `depth - 1`, we initialize two new `TreeNode` objects as described by the problem, linking them with the children of the current node accordingly. Otherwise, we continue traversing the tree by enqueueing each child(if it exists) along with their depths.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. Performing a BFS traversal on a tree with $n$ nodes takes $O(n)$ time. And since processing each node takes $O(1)$ time, the overall time complexity becomes $O(n)$. The space complexity is also $O(n)$, as we use a queue to store nodes to be visited in the future.  
  

