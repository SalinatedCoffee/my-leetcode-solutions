## 107. (M) Binary Tree Level Order Traversal II

### `solution.py`
Given a binary tree's root node `root`, we are asked to return the 2D list of nodes in left to right reverse level order. This can be easily achieved by traversing the tree using DFS while keeping track of the depth of each node. Once the traversal ends, we will end up with a level order list of nodes in the tree which can be reversed to satisfy the problem's requirements. Note that the current node can be processed at any time as long as the left subtree is explored first, since nodes at different depths will have their values added to different lists. Thus preorder(NLR), inorder(LNR), and postorder(LRN) traversals are all viable, as well as traversing the tree using BFS instead of DFS.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the binary tree rooted at `root`. Traversing the tree takes $O(n)$ time, as well as reversing the level order list of node values. The space complexity is also $O(n)$, due to the recursion stack.  
  

### `solution_2.py`
As mentioned above, we may traverse the tree however we want as along as we make sure that it is traversed left to right. In the previous solution we had implemented a recursive preorder traversal, generating a level order list of the nodes and reversing it afterwords. Here, we will implement a iterative postorder traversal purely as practice. Iterative implementations of non-preorder traversals are typically more involved as a node is not naturally revisited after it has been traversed, unlike the recursive implementations.  
We first take the root and traverse down towards the far left, pushing the traversed node back onto the stack as we do so. When we reach a node that does not have a left child, there are 3 possibilities depending on the node currently on top of the stack. If the node has no right child, it means that the parent node of the last traversed left node has no right child and its value should be processed. If the node has a right child but it has already been traversed, it means that both subtrees of the current node have been traversed and its value should be processed. If the node has a right child that has *not* been traversed, we traverse to the child without doing anything else. Once the stack is empty and the current node is `None`, we will have fully traversed the binary tree. After trimming off the empty list at the end of `ret`, we reverse `ret` before returning it.  

#### Conclusion
The time and space complexity of this solution is identical to the previous solution.  
  

