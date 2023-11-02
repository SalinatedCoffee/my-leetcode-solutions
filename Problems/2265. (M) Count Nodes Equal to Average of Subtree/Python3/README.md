## 2265. (M) Count Nodes Equal to Average of Subtree

### `solution.py`
In order to compute the average value of a tree rooted at some node `i`, we need the sum of the node values and the size of the left and right subtrees of `i`, if they exist. These values can be easily retrieved by recursively traversing the tree, where the recursive function returns a tuple containing the sum and number of nodes. After recursing on a node's children we compute the average value of the tree, and increment a counter if the average equals the root's value.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the number of nodes in the tree rooted at node `root`. The space complexity is also $O(n)$ since the recursion stack has a size of $O(h)$, where $h$ is the height of the tree. Because the tree is not guaranteed to be balanced, $h = n$, and thus the recursion stack will use $O(n)$ memory.  
  

