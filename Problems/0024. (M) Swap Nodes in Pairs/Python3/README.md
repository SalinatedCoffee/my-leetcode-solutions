## 24. (M) Swap Nodes in Pairs

### `solution.py`
The principle is rather simple in that we simply want to iterate along the linked list in pairs. For each pair we swap them, connect the left node to the previous right node, and move on. Here the implementation uses iteration, which means we need to keep track of the previous pair's right node separately. If we had used recursion we could have set it up so that the recursive call returns the node that needs connecting instead. Since the while loop exits when either node does not exist we need to remember to properly terminate the last pair of nodes; either connect it to the sole node if it exists, or make it a null pointer.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of the given linked list. The linked list is traversed once, hence the linear running time. The space complexity is $O(1)$.  
  

