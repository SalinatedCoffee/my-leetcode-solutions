## 61. (M) Rotate List

### `solution.py`
Given a singly linked list(the head node `head`) and integer `k`, we are asked to return the head node of the original linked list rotated `k` times towards the right. For example, if the original list is `1 -> 2 -> 3 -> 4 -> 5` and `k = 2`, the resulting list would be `4 -> 5 -> 1 -> 2 -> 3`.  
The immediate thought that comes to mind is that we can perform just `k % n` rotations(where `n` is the length of the linked list) instead of `k`, since rotating the list by `n` would result in an identical list. Once we have the value of `k` modulo `n`, rotating the list is trivial(albeit slightly annoying).  
When `rotateRight` is called, we first check the value of `head` to see if we were actually given a linked list. If it is `None`, we simply return `None`. Then, we make a single pass over the entire linked list, counting the number of nodes and keeping a reference to the tail node. Now that we have the value of `n`, we can compute the value of `k` modulo `n`. If this value is `0`, we immediately return `head`. Otherwise, we traverse the list up to the `n - k % n`th node, splice the linked list, and return the head node of the new linked list.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of the singly linked node that has `head` as its head node. The entirety of the linked list is traversed at most twice, with each node taking $O(1)$ time to process. Rotating the list is also a $O(1)$ time operation, which brings the overall time complexity to $O(n)$. The space complexity is $O(1)$.  
  

