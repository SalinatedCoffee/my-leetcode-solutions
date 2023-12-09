## 94. (E) Binary Tree Inorder Traversal

### `solution.py`
This is a problem that can be trivially solved by implementing a recursive DFS traversal. `dfs(node)` first examines whether `node` has a left child. If it does, it recurses on the next child. Next, it appends `node`'s value to the return list `ret`. Lastly it recurses on `node`'s right child, if it exists.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. Traversing a binary tree with $n$ takes $O(n)$ time. Excluding the return list `ret` the recursion stack will use $O(n)$ memory as the recursion tree can be at most $n$ levels deep.  
  


### `solution_2.py`
The iterative version is a bit more involved as we cannot directly translate the recursive algorithm into the iterative version. If we think about the behavior of `dfs()` in the previous solution, it essentially keeps pushing nodes on the recursion stack as long as it has a left child. If it doesn't, it appends the current node's value onto the return list and then recurses on its right child if it exists. We can implement this behavior in an iterative algorithm using a few conditionals inside a loop. If the current node has a left child it is pushed to the stack and the loop is continued. If not, we pop a node off of the stack, add its value to `ret`, and push its right child onto the stack. We are done when the stack is empty and there are no nodes to process, at which point we break out of the loop and return `ret`.  

#### Conclusion
This solution has the same time and space complexity as the previous solution.  
  
