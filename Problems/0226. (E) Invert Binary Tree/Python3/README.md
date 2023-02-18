## 226. (E) Invert Binary Tree

### `solution.py`
Obviously, the easier way would be to swap subtrees from the bottom-up. We can trivially do this by implementing a recursive function that first recursively switches its children before returning itself.  
  
#### Conclusion
The time complexity is $O(n)$ where $n$ is the number of nodes in the tree. The space complexity is als $O(n)$ since the maximum size of the recursion stack will be the height of the tree, which at worst can be of size $n$.  
Note that this problem could also be solved by using a (iterative) BFS-like approach, where we swap subtrees of nodes depth-by-depth.  
  

