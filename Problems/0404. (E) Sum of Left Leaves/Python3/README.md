## 404. (E) Sum of Left Leaves

### `solution.py`
This problem can be solved by simply passing additional information about a node's ancestry while traversing the tree. For this problem we have opted to implement the recursive flavor of DFS. If we modify the given function signature to include an additional boolean value, we can use this to check whether a node is a left child of its parent. If the current node is a leaf, we return its value if the boolean is `True` and `0` otherwise. If the node is not a leaf, we recurse on its children, passing in `True` as the additional parameter for the left child.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the given tree. DFS takes $O(|V|)$ time to traverse a graph, where $V$ is the set of vertices within that graph. For this problem, $V$ is simply $n$, hence the time complexity of $O(n)$ for the DFS component. Each visited node takes $O(1)$ time to process, and thus the overall time complexity is $O(n)$. The space complexity is also $O(n)$, as the recursion stack is proportional to the height of the tree being traversed. As the given tree is not guaranteed to be balanced, the height is $O(n)$.  
  

