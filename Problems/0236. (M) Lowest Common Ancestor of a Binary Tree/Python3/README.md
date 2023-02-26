## 236. (M) Lowest Common Ancestor of a Binary Tree

### `solution.py`
Since this problem deals with general binary trees we cannot simply reuse the solution to [problem #235](../../0235.%20(M)%20Lowest%20Common%20Ancestor%20of%20a%20Binary%20Search%20Tree/Python3/README.md). A simple and still relatively fast way to solve the problem is to traverse the tree while building paths to nodes `p` and `q`. Once we have the paths from the root to the two nodes we just have to iterate through both paths and find the last node that is identical between the two.  
  
#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is the number of nodes in the tree. Traversing the tree takes $O(n)$ time, and the recursion stack along with the paths to `p` and `q` use $O(n)$ memory.  
Traversing the tree once and looking for `p` and `q` simultaneously may benefit performance in terms of running time.  
  
