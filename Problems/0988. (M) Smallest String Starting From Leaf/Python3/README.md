## 988. (M) Smallest String Starting From Leaf

### `solution.py`
We can easily find all strings by performing a DFS traversal on the given tree. If we maintain a stack of characters in the current traversed 'branch', we can generate the string whenever we find a leaf by reversing the stack and concatenating its contents. Because we are converting the node values into a string upon detecting a leaf, we can simply delegate the actual string comparison to Python, which behaves exactly the same as described by the problem. If the string is lexicographically smaller than the current smallest, we make the smaller string the current smallest and continue traversing the tree.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$ where $n$ is the number of nodes in the tree rooted at `root`. Traversing the tree with DFS takes $O(n)$ time. Whenever a leaf node is encountered, we construct the corresponding string by first reversing the stack of characters in the current path and concatenating them into a string. This takes $O(n)$ time, as the height of the tree is bound by $O(n)$ because it is not guaranteed to be balanced. The conversion is performed for all leaf nodes in the given tree, of which there are $O(\log n)$ of since it is a binary tree. Hence, because it takes $O(n)$ time to traverse the tree, and $O(n)$ time to process a leaf node which there are $O(\log n)$ of, the overall time complexity becomes $O(n + n\log n) = O(n\log n)$. The space complexity is $O(n)$, due to the recursion stack and stack of characters `self.stack`.  
  

