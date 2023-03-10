## 144. (E) Binary Tree Preorder Traversal

### `solution.py`
A preorder traversal of a binary tree involves consuming the nodes in this order: `N -> L -> R`. This is trivial to implement recursively, as is shown in the solution.  

#### Conclusion
All nodes are visited exactly once, thus the time complexity for this solution is $O(n)$ where $n$ is the number of nodes. Since it implicitly uses a stack through recursion the space complexity is $O(h)$, where $h$ is the height of the tree being traversed. This is because two nodes are added each level and one is 'popped off' the recursion stack, which means one node is added to the stack every time we traverse down(up? trees are weird) one level. Naturally the deepest level we can reach is exactly the height of the tree, hence the worst case space complexity of $O(h)$.  
[Morris traversal](https://www.geeksforgeeks.org/?p=6358) may make for some interesting extra reading - it basically modifies the given tree which allows it to run in $O(n)$ time with $O(1)$ space. Downsides are that it, well, modifies the given input and in practice runs slower than simple depth-based traversals due to extra pointer operations.
  

### `solution_2.py`
Same idea as the first solution, but implemented using iteration for completeness.  
#### Conclusion
Refer to the first solution analysis.  

