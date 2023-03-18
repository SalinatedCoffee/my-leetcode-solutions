## 129. (M) Sum Root to Leaf Numbers

### `solution.py`
The solution involves paths from the root to all leaves, and thus can be trivially solved with recursive DFS. The base case is when the provided node is `None`, in which case we return `0`. If both recursive calls to a node's children returns `0`, that would mean that the node is a leaf, and so we return the total value up to that point. Otherwise, we simply return the sum of the recursive calls.  

#### Conclusion
This solution has a running time of $O(n)$ where $n$ is the number of nodes in the tree. The space complexity is also $O(n)$.  
  

