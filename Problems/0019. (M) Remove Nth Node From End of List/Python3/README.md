## 19. (M) Remove Nth Node From End of List

### `solution.py`
A trivial solution to this problem is to simply iterate over the list while saving references to each node in a list. Then, we can directly access the `n`th node from the tail and remove it from the list. This approach however, requires $O(n)$ extra space where $n$ is the length of the given linked list. Instead, we can do better by using two pointers instead of a single pointer and a list.  
The premise is rather simple; we simply delay one pointer by `n` nodes and keep advancing both pointers at the same rate until the 'lead' pointer reaches the tail. At that point the delayed pointer will be pointing to the `n`th node from the tail, which is exactly what we want. First we initialize two pointers and make the. point to `head`. Then we advance one pointer `n` nodes, and check whether it already points to the tail. If so it means that we have been asked to remove `head` from the list, and we return `head.next`. Otherwise, we start advancing both pointers until the lead pointer points to the tail node. At this point, the delayed pointer will be pointing to the *previous* node of the node that we want to remove. We remove the target node accordingly, and return `head`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the number of nodes in the given linked list. The linked list is iterated over exactly once, with each node taking $O(1)$ time to process. The space complexity is $O(1)$, as we only use a handful of variables with fixed size.  
  

