## 1161. (M) Maximum Level Sum of a Binary Tree

### `solution.py`

Computing the per-level sums is simple, since a BFS traversal will naturally traverse nodes in level order. The phrase "*Return the **smallest** level `x` such that the sum of all the values of nodes at level `x` is **maximal**.*" may be confusing at first, but in the end this simply means that we should return the highest level if there are multiple levels with the same value, which is the maximum sum. This can be naturally found by iterating over the level sum array in reverse order.  

#### Conclusion

The time complexity is $O(n)$, where $n$ is the number of nodes in the tree. BFS touches each node exactly once, and the maximum search takes $O(n)$ times since the number of levels is the height of the tree, which is $O(n)$ as the tree is not balanced. The space complexity is also $O(n)$.  


