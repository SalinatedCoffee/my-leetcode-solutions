## 951. (M) Flip Equivalent Binary Trees

### `solution.py`
Given the root nodes of two binary trees, we are asked to determine whether the two trees are 'flip equivalent'. Two binary trees are flip equivalent if one tree can be modified to exactly match the other tree by swapping the left and right child of any node, for any number of nodes. We can easily verify this by first checking the current pair of nodes, and then recursively checking the matching pairs of the subtrees of the current pair of nodes.  
When `flipEquiv` is first called, we examine `root1` and `root2` to check if they are equal. If only one of them is `None`, or their values do not match, we can immediately return `False` as the two trees are not flip equivalent. Otherwise, we try matching the children of `root1` and `root2`. Only when all present children can be matched can the trees potentially be flip equivalent, and so we return `False` if all children cannot be matched into pairs. If all children have been matched, we recurse down on each pair and logical AND all return values, which we can directly return.  

#### Conclusion
This solution has a time complexity of $O(\min(m, n))$, where $m$ and $n$ is the number of nodes in the binary tree rooted at `root1` and `root2`, respectively. In the worst case(both trees already match, or are flip equivalent), the entirety of both trees are traversed. In other cases, the recursion stops immediately when a mismatch is found, which includes that arising from absent nodes. Since processing a single node pair requires $O(1)$ time to complete, the overall time complexity becomes $O(\min(m, n))$. The space complexity is also $O(\min(m, n))$, due to the recursion stack.  
  

