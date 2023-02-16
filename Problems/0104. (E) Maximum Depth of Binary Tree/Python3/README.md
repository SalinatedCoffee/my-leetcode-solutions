## 104. (E) Maximum Depth of Binary Tree

### `solution.py`
To determine the maximum depth of a binary tree we should use DFS. A recursive algorithm can be trivially implemented by returning the depth of the larger subtree + 1.  

#### Conclusion
The solution runs in $O(n)$ time and space, where $n$ is the number of nodes in the tree. DFS traverses each node exactly once, hence the time complexity of $O(n)$. The recursion stack at most is the same size as the depth of the given tree which is $O(n)$.  
  

### `solution_2.py`
This solution uses the iterative version of DFS, added here for completeness.  

#### Conclusion
This solution has the same time and space complexity as the first solution. A list takes the place of the recursion stack, with the same scaling behavior.  
  

