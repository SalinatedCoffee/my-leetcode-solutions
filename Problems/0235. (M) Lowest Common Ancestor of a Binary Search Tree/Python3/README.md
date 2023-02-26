## 235. (M) Lowest Common Ancestor of a Binary Search Tree

### `solution.py`
The given tree is a binary search tree, where the left subtree of a node only contains nodes with smaller or equal values to the current node's, and larger values in the right subtree. Say we are at some node with a value that is smaller than both `p` and `q`. In this case, *both* `p` and `q` will be in the right subtree as they have values larger than the current node. The opposite is also true where `p` and `q` will be in the left subtree if both nodes have smaller values than the current node. In both of these situations the node in question can't possibly be a common ancestor of `p` and `q`. Taking the inverse of this statement then, we get that a node *is* a common ancestor of `p` and `q` if its value is between (inclusively) their values. We can also conclude that the *first* node that satisfies this condition during a preorder traversal is also the lowest common ancestor of `p` and `q`, since the traversal recursively enumerates nodes from the shallowest depth to the deepest. Thus, we simply need to implement a preorder traversal algorithm that also checks whether the value of the current node is between those of nodes `p` and `q`.  

#### Conclusion
This solution takes $O(n)$ time and space to run where $n$ is the number of nodes in the BST.   
  

