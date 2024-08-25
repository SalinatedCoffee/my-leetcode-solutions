## 145. (E) Binary Tree Postorder Traversal

### `solution.py`
Given the node `root`, which is the root node of a binary tree, we are asked to return the postorder list of node values. This can be trivially achieved by traversing the tree recursively, recursing down on the left and right child(in that order) before adding the value of the node to the list of node values.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. The space complexity is also $O(n)$, due to the recursion stack.  
  

### `solution_2.py`
The same traversal algorithm can also be implemented iteratively, using a stack to explicitly keep track of to-be-visited nodes instead of the call stack. While the idea of visiting all child nodes before recording the value of the current node is the same, the actual implementation is slightly more involved. Unlike the recursive implementation, we need to recognize when the current node should be 'deferred' for processing and manually push it back onto the stack. If we lay out the things that happens upon reaching some node `node` in a tree in a list, it would look something like this:  
 1. `node` is visited.
 2. We leave `node` and move to `node.left` if it exists.
 3. After visiting all the nodes in the left subtree of `node`, we visit `node` a second time.
 4. We leave `node` and move to `node.right` if it exists.
 5. After visiting all the nodes in the right subtree of `node`, we visit `node` a third time.
 6. The value of `node` is added to the list of node values before leaving `node`.
Looking at this list, we can see that `node` must be revisited after visiting any one of its children. Hence, `node` should be pushed back onto the stack whenever the traversal algorithm moves onto its children.  
We first begin by traversing down the left as far as we can go, while also pushing the right child of these nodes if it exists. Once we reach a 'dead end', we look at the children of the current node to determine our next move. If it has no children, it is a leaf node and we should append its value to the end of the list of node values. If it has a right child, and the right child is on top of the stack, we move to the right child and repeat the previous steps.  

#### Conclusion
The time and space complexity of this solution is identical to the previous one, but will run faster in practice since it does not have the overhead that comes from recursive function calls.  
  

