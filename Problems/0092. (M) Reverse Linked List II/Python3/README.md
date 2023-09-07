## 92. (M) Reverse Linked List II

### `solution.py`
When given `left` and `right` and the `head` of a linked list, we are asked to reverse the section starting with the `left`-th node (1-indexed) up to the `right`-th node. The follow-up question also asks us to implement a 1-pass solution, which is straightforward to do. Reversing a linked list in-place is trivial, and since we are given the positions of where the reversed section begins and ends, we can simply walk across the list while reversing nodes that are within the reversed section. Once the reversing is complete we need to know 4 things in order to splice the sections back together. The tail node of the left untouched section, the head node of the right untouched section, and the head and tail node of the reversed section. We can keep track of these nodes simply by walking through the list, and if we do so while performing the reversing step we can avoid having to traverse the list twice.  
One last detail to keep in mind before returning is that it may be the case that the entire list is reversed (`1 == left` and `n == last`), in which case we cannot return `head` and instead should return `rev_head` - the head of the reversed section (or the tail of the original list).  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of the linked list starting with node `head`. We traverse the list exactly once, and at each node only a handful of constant-time operations are performed hence the   
