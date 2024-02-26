## 100. (E) Same Tree

### `solution.py`
This problem is trivial to solve; we simply traverse the two trees simultaneously using the same traversal algorithm. No gotchas, no weird inputs, no time constraints. Here we have opted to use an iterative DFS-based approach using two stacks. Whenever we encounter a discrepancy between the two trees (one node does not exist or nodes have different values) we return `False`.  

#### Conclusion
As is the case for any depth-first tree traversal this solution runs in $O(n)$ time using $O(n)$ memory, where $n$ is the number of nodes in one tree. Because the worst case is when both trees are identical to one another it does not matter which tree we refer to in this analysis. Since the trees are not guaranteed to be balanced, the height can be at most $n$. The memory usage of the stacks scale linearly with the height of the trees, hence the space complexity of $O(n)$.  

### `solution_2.py`
This solution is the recursive flavor of the first one, added here for completeness.  
  
#### Conclusion
Same running time and space complexity as the first solution, but in practice runs slower and uses less memory by comparison. The iterative solution is fast since `pop()` and `append()` on Python lists are much faster compared to recursive function calls(unrelated, but [here's](https://wiki.python.org/moin/TimeComplexity) the official time complexity reference for Python collections). On the flip side, the recursive solution uses less memory since it only needs to maintain one recursion stack compared to two lists in the iterative solution.  
 
