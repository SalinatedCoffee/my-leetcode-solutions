## 101. (E) Symmetric Tree

### `solution.py`
We know that we could use recursion to solve this problem, but how we should be traversing the tree is not that obvious. For a tree to be symmetric, it must be mirrored about the center. That tells us that we should traverse the nodes in a similar fashion, where we branch either inwards or outwards. Also, we are determining whether the *entire* tree is symmetric or not so we shouldn't recurse on a single node.  
A separate recursive function is declared, where the provided function acts as a wrapper. It is provided with two nodes, and the base cases are when both nodes are the same (including `None`) and when they are not. Then, the subtrees rooted at their children are checked by recursively comparing the children branching outwards (`left.left` and `right.right`) *and* inwards (`left.right` and `right.left`).  
  
#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. The space complexity is $O(h)$ where $h$ is the height of the tree. A tree can have a height of $O(n)$ only when it is not symmetric, and the recursion exits early whenever a mismatch is found - hence the recursion stack of $O(h)$.  
  

