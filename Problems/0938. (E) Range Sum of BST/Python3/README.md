## 938. (E) Range Sum of BST

### `solution.py`
Because the range in given in terms of the nodes' values, we can simply traverse the tree rooted at `root` while directly checking whether a node's value falls in the desired range. For this problem, we have opted to implement the iterative flavor of DFS. At each node we determine whether its value is in the interval `[low, high]`. If so, we add it to `ret`; otherwise, we simply do nothing before adding its children to the stack of to-be-traversed nodes. Once the entire tree has been traversed, we can directly return `ret`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the binary search tree rooted at `root`. DFS has a time complexity of $O(|E|+|V|)$, where $|E|$ and $|V|$ are the number of edges and vertices(nodes) in the tree being traversed, respectively. Because the given tree is a binary search tree, it will contain $n-1$ edges; hence the overall time complexity of $O(n+n-1) = O(n)$. The space complexity is also $O(n)$. `nodes` has a space complexity of $O(h)$, where $h$ is the height of the tree being traversed. While the given trees are BSTs, they are not guaranteed to be balanced; hence the space complexity becomes $O(h) = O(n)$.  
  

