## 1382. (M) Balance a Binary Search Tree

### `solution.py`
The first thing that comes to mind are AVL trees and their rebalancing algorithms. Self-balancing trees maintain their balance by constantly rotating nodes however, which unfortunately makes this approach infeasible for this particular problem. There is a much easier way if we do not mind using some extra memory though, which takes advantage of the fact that creating a balanced tree is easier than rebalancing one. The given tree is still a binary search tree, which means that performing an inorder traversal on it will yield a list of nodes in ascending order. We can first traverse the tree and generate the ordered list of nodes, and then use that list to create a balanced copy of the binary search tree.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the tree rooted at `root`. Traversing the tree takes $O(n)$ time, with the construction step taking the same amount of time. The space complexity is also $O(n)$ since we keep a list of all nodes in memory.  
If we want to reuse the nodes of the given tree, we could simply store the references of the nodes in the list instead of their values.  
In order to avoid using any extra memory, we need to resort to an in-place balancing algorithm called the [Day-Stout-Warren algorithm](https://en.wikipedia.org/wiki/Day%E2%80%93Stout%E2%80%93Warren_algorithm), which first converts the tree into a vine and then the vine back into a balanced tree. The time complexity of this algorithm is also $O(n)$.  

