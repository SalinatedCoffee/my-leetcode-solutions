## 783. (E) Minimum Distance Between BST Nodes

### `solution.py`
This problem would have been a lot more difficult if the tree wasn't a search tree. Thankfully it is, so we can just traverse the tree inorder (LNR) to retrieve the nodes in ascending order. The solution simply generates the inorder list of nodes and iterates across it to determine the minimum difference.  
  
#### Conclusion
This solution runs in $O(n)$ time and space, where $n$ is the number of nodes in the tree. The inorder traversal touches every node exactly once, and the inorder list `self.vals` contains $n$ number of elements.  
  

### `solution_2.py`
Instead of generating an inorder list of nodes we can remember the value of the previous inorder node and update the minimum difference during the traversal.  
  
#### Conclusion
The solution runs in $O(n)$ time but uses $O(1)$ space since `min_diff` is determined during traversal instead of iterating over a list of size $n$.  
  