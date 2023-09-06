## 725. (M) Split Linked List in Parts

### `solution.py`
The difficulty of this problem comes from the fact that we are not given the length of the linked list beforehand. We can however simply iterate along the list to determine its length, which trivializes this problem.  
We are asked to split the given linked list into `k` pieces. If this list has a length of `n`, each piece should be `n // k` nodes big, with one extra node for the first `n % k` pieces. Based on these values, we simply compute the size the `i`th piece should be and advance through the linked list `size - 1` times (thus touching `size` nodes including the node we started at). At that point we have reached the last node of the list, and so we disconnect the node from the list and move the pointer to the next node in order to process the next piece. After appending the head of the current piece to the return list `ret`, we repeat this process `k - 1` times to create the required `k` pieces of the original linked list.  
Note that we have to take into account cases where `k` is larger than `n`; that is, we are asked to split the list into more pieces than its number of nodes. In this case `size` will be `0` and `r` will be `n`, and so no additional work needs to be done. During the splitting step however, we will need to handle the case where the pointer runs off the linked list and is `None`. If this is the case, we must explicitly denote that the piece is empty by appending `None` to the return list(in other words, the return list must be `k` long).  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of the linked list starting with node `head`. The linked list is iterated over twice; once to determine its length, and once more to split it into `k` pieces. A fixed number of constant-time operations are performed for each node, hence the overall time complexity of $O(n)$. The space complexity is $O(1)$.  
  

