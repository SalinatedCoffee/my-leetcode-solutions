## 1721. (M) Swapping Nodes in a Linked List

### `solution.py`

There are multiple methods of solving this problem, with one of the easier ways being simply storing references to the nodes in an indexable list. We simply traverse the linked list while appending each node to the list `nodes`, which lets us access the `i`th node in constant time.  

Perhaps a more useful method (which is more generalizable) would be to swap the two *nodes* instead of simply swapping their values. A solution involving a dummy 'sentinel' node at the head to deal with edge cases would also most likely work.  

#### Conclusion

This solution has a time and space complexity of $O(n)$ where $n$ is the length of the linked list. The LL is traversed once, and `nodes` will contain references to all nodes in the LL.  
