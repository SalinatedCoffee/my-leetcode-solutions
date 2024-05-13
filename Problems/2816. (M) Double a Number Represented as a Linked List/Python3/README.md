## 2816. (M) Double a Number Represented as a Linked List

### `solution.py`
The easiest solution is to traverse the list and store references to each node in a separate list. We can then iterate over the list in reverse order(thereby starting with the least significant digit) while doubling the value of each node. Of course, we also need to keep track of the carry while we do so, remembering to create a new head node if it is a non-zero value after doubling all available digits.  

#### Conclusion
This solution has a time and space complexity of $O(n)$. The first pass over the linked list, as well as the doubling step that follows it, each take $O(n)$ time to complete. The references to each node in the linked list is stored in the separate list `nodes`, which uses $O(n)$ memory since there are $n$ nodes in the linked list.  
  

