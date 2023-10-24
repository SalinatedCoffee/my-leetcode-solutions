## 515. (M) Find Largest Value in Each Tree Row

### `solution.py`
As we want the maximum node value for each level, naturally we would want to traverse the tree in level order as well. This can easily be accomplished by traversing the tree using BFS, and labeling the nodes with its depth as they are added to the queue.  
We first initialize a dictionary `rowmax`, with default values of `float('-inf')`. `rowmax[i]` will contain the maximum node value for the row `i`. Using the queue `nodes` we can now begin traversing the tree, while updating the appropriate `rowmax`. Once the traversal has completed, we sort `rowmax` by its keys (depths) and return the resulting list of values.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. BFS has a time complexity of $O(|V|+|E|)$ that simplifies into $O(n)$ since a binary tree is being traversed. The space complexity is also $O(n)$, due to `nodes`.  
  

