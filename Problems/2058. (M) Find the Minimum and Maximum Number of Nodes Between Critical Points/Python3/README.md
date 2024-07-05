## 2058. (M) Find the Minimum and Maximum Number of Nodes Between Critical Points

### `solution.py`
Given a linked list of integers, we are asked to determine the minimum and maximum distance between two critical points. A critical point is defined as a node that is either larger than or smaller than its two neighboring nodes. As such, a node with only one neighbor(the head and tail nodes) *cannot* be a critical point. Coming up with the algorithm is simple, but(as is typically the case with linked list problems) the actual code is rather annoying to implement. For the distance, it is quite obvious that the minimum distance will be found between any two adjacent critical points and the maximum will be the distance between the first and last critical points. We first find the first critical point in the linked list. After saving the index of the first critical point(if it exists) in a separate variable, we continue iterating over the remainder of the list while computing the distance of two adjacent critical points. Once the iteration completes, we look at the distances to determine whether there are at least 2 critical points in the list and return the appopriate value.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of the linked list starting at node `head`. The given linked list is iterated over exactly once, and since each node takes $O(1)$ time to process, the overall time complexity is $O(n)$. The space complexity is $O(1)$.  
  

