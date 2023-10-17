## 1361. (M) Validate Binary Tree Nodes

### `solution.py`
Essentially, the problem is asking us to verify the following; there is exactly one root that has no parent, there are no cycles, and all nodes are reachable from the root. Hence, we may use any graph traversal algorithm to traverse the given tree to determine whether it is a valid binary tree or not. For this solution we have chosen to implement the iterative flavor of BFS. Starting the traversal from the root, if at any point a node is traversed more than once, a cycle exists in the graph and we can immediately return `False`. After the traversal has completed, if the number of visited nodes is not equal to `n`, it means that not all nodes were reachable from the root and we return `False`. A detail that is easily missed is that any node can be the root, and we thus have to find a candidate root before starting the traversal. This can be easily done by searching for a root without a parent; that is, a node that does not appear in both `leftChild` and `rightChild`. If more than 1 such node exists, we may immediately return `False` as that would indicate the existance of multiple root nodes.  
Note that the problem could also be solved using union-find, with the trade-off being complexity and overhead in exchange for correctness.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is `n`. Searching for the root takes $O(n)$ time, and since BFS takes $O(|V|+|E|)$ time where $|V| = n$ and $|E| \leq n-1$, the traversal step also takes $O(n)$ time. The space complexity is also $O(n)$, as `leftChild` and `rightChild` have a length of $n$, and `visited` and `nodes` will use $O(n)$ memory.  
  

