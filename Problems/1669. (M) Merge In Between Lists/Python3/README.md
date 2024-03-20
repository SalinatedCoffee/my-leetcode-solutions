## 1669. (M) Merge In Between Lists

### `solution.py`
A rather straightforward problem despite being tagged as medium, we only need references to 3 nodes in order to perform the merge. We need a reference to the `a-1`th node and `b+1`th node from `list1`, and the tail node of `list2`. Once we have access to the three nodes, we can simply link the `a-1`th node to the head node of `list2` and the tail node of `list2` to the `b+1`th node to merge the 2 lists as required. One edge case we need to keep in mind is when `a = 0`, which means that the head of the merged list is that of `list2`.  
If you come from C/C++ (and are cringing after reading the solution code) it would of course be good practice to properly terminate dangling references with `NULL`. This, I leave as an exercise to the reader as it is not that difficult to implement.  

#### Conclusion
This solution has a time complexity of $O(m+n)$ where $m$ and $n$ are the lengths of the linked lists that have `list1` and `list2` as their head nodes, respectively. Retrieving the references to the required nodes entails traversing both linked lists, which each takes $O(m)$ and $O(n)$ time to complete. The space complexity is $O(1)$, as we only use a handful of pointers during the entire runtime of the algorithm.  
  

