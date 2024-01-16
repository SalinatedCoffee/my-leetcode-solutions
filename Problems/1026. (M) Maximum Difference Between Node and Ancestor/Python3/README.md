## 1026. (M) Maximum Difference Between Node and Ancestor

### `solution.py`
Given a tree, we are asked to return the maximum difference between two nodes `a` and `b` where `a` is a descendent of `b`(and vice versa). We know that when traversing a tree starting at the root, we would have already visited all of the ancestors of the node that is currently being visited. Using this fact, we can compute the maximum difference between the current node and its ancestors. Instead of passing down the values of all of the ancestors of the current node, we only need to know the minimum and maximum values of its ancestors. However we also want to know the maximum difference for each of its subtrees(if they exist), which can also be easily determined by recursing down on the child nodes.  
We define the function `dfs(node, s, l)`, which is a slightly modified version of recursive DFS. It returns the maximum difference for the subtree rooted at node `node`, where the smallest and largest values of the ancestors of `node` are `s` and `l`, respectively. The difference of `node` and its ancestors are first computed, after which the algorithm recursed down the left and right children with updated values for `s` and `l`. By definition of the function `dfs`, the value we want is the return value of `dfs(root, root.val, root.val)` (it is guaranteed that at least 2 nodes exist in the tree, and we want the absolute difference of values, which is why we can pass in `root.val` for `s` and `l`) which we can return directly.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the tree rooted at `root`. DFS takes $O(|E| + |V|)$ time to complete, and since we are traversing a tree the overall time complexity becomes $O((n-1)+n) = O(n+n) = O(n))$. The space complexity is also $O(n)$. There is no guarantee that the tree is balanced, and so the height of the tree becomes $O(n)$. The maximum height of the recursion stack is the height of the tree being traversed, which we have already established to be $O(n)$. Thus, the overall space complexity is $O(n)$.  
  
