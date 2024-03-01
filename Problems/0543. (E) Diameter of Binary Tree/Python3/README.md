## 543. (E) Diameter of Binary Tree

### `solution.py`
The problem may seem trivial at first glance, but there is a slight nuance to it. As explained in the problem description, the longest path between two nodes may not always go through the root. Thus at every node we must check whether the path going through it is the longest. There are many ways to implement this approach, but here we have opted to store the path length in a global variable and have the recursive function return the longest branch length in the tree rooted at the input node.  
Say we have a tree rooted at node `root`. If we were to construct the longest path that goes through `root`, what paths should we choose from `root`'s children? For one, we cannot choose a path that goes *through* a child as that would involve branching off the path towards `root`, making the path invalid. Obviously then we would want to select the longest path that starts (or stops, depending on perspective) at the child, since we can legally extend that path to `root`. Using this logic we can implement a recursive function `recurse(node)` that returns the length of the longest path that terminates at `node`. We first recurse on `node`'s children, which will return their path lengths. Then we select the longer path of the two, and return that value + 1. As mentioned previously, we also need to remember to update the longest path in the entire tree before exiting. The length of the longest path passing through `node` is simply the sum of those of `node`'s children + 2. Once the recursion exits, we need only return the value of the global length variable, which in our implentation is `ret`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. `recurse` effectively performs a recursive DFS traversal on the given tree, which takes $O(n)$ time to complete since each node is visited exactly once. The space complexity is also $O(n)$ as the recursion stack scales linearly with the depth of the tree, which can be at most $n$ since the provided tree is not guaranteed to be balanced.  
  
