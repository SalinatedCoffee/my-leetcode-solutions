## 23. (H) Merge k Sorted Lists

### `solution.py`
While the individual lists are sorted, the heads of those lists are not in ascending order. Among the pool of head nodes of all linked lists, we want to access the node with the smallest value in an efficient manner. We can use python's `heapq` for this, remembering to use some counter as a tiebreaker. The heap queue is first populated by examining the head nodes of all lists in `lists`. We then keep popping a node from the queue, linking it to the previous processed node, and then pushing the next node if it exists.  
Once the iteration has completed we simply need to return the very first node that has been processed.  
  
#### Conclusion
The time complexity is $O(n\log n)$ where $n$ is the sum of all nodes in `lists` since push/pop operations take $O(\log n)$ time, which we perform $2n$ times. The space complexity is $O(m)$ where $m$ is the length of `lists`.  
  

