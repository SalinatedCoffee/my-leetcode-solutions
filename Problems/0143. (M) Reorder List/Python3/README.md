## 143. (M) Reorder List

### `solution.py`
First off, we don't know how long the linked list is so we must iterate through it at least once. Also since the list is singly linked we need to either somehow figure out a way to access all nodes in constant time or iterate through it another time to reverse the order.  
For the actual reordering, the problem is asking us to 'split' the list into half (with the middle node being the tail of the left side if the list is of odd length) and then weave the halves together with the right side being in reversed order.  
If we have constant time access to all nodes this becomes trivial, so we can simply add all nodes to a queue (or a list, array, etc) and connect the nodes at both ends of the queue. Then we connect the end of this pair to the first node of the next pair and so on, and so forth until the queue contains less than 2 elements. The queue will still contain one node if the linked list had an odd number of nodes, which we make the tail of the reordered list as requested by the problem.  
  
#### Conclusion
The solution uses $O(n)$ time and space where $n$ is the number of nodes in the given linked list.    


### `solution_2.py`
We can also solve this problem without maintaining references to all nodes, however we will need to traverse the list multiple times to achieve this. We first use the slow/fast pointer method to get the reference to the first node in the latter half. The slow pointer advances by one, and the fast pointer advances by two; so when the fast pointer reaches the end of the list the slow pointer will be pointing to the desired node.  
Now we traverse the latter half while reversing the list order, which is trivial to implement. Finally we interleave the two lists together, remembering to terminate the list with a `None` if the list has an odd number of nodes.  
  
#### Conslusion
This solution uses $O(n)$ time but uses $O(1)$ space.  
  
  
