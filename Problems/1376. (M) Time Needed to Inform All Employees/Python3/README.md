## 1376. (M) Time Needed to Inform All Employees

### `solution.py`

Going down the chain of command and informing two different employees can happen simultaneously, and thus we want the amount of time it takes to inform the last employee(or the maximum time it takes to inform one employee). The time it takes to inform an employee then, is simply the sum of `informTime` of all nodes in the path from the root, excluding itself. Since this sum only increases it stands to reason that a leaf node will take the longest to notify than any other nodes in the path; hence, the last employee to be informed will **always** be a leaf node.  

Now we may simply traverse the graph (iterative DFS is used in this implementation) while updating the maximum time accordingly whenever a leaf node is traversed, and return that value once the traversal has completed.  



#### Conclusion

This solution has a time complexity of $O(n)$ where $n$ is simply `n`. Constructing the adjacency list and traversing the tree both takes $O(n)$ time. The space complexity is also $O(n)$, since `nodes` uses $O(n)$ memory.  


