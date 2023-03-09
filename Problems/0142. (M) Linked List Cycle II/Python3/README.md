## 142. (M) Linked List Cycle II

### `solution.py`
The non-$O(1)$ memory solution where a set is used to store previously traversed nodes is trivial to implement. We can do it with constant memory, by using a two pointer approach. If we advance one pointer by 1, and the other by 2, they will inevitably end up pointing to the same node at some point in time if a cycle exists. The problem now becomes finding the next node of the 'tail', as the node from the cycle detection step is not necessarily the one we want. However we know how many nodes the tail skips to, which is the distance traveled by the slow pointer. Letting `i` be this distance we know we want the `n-i`th node. We don't know where the 'tail' is, so we have to determine this node starting at `head`. Two pointers can be used here as well, where we give one a 'head start' of `i` nodes(in other words, the slow node is `i` nodes behind the fast one). Now when we advance both nodes by 1 the fast pointer will meet the slow pointer at the `n-i`th node as when the fast node moves to the `n+1`th node looping back to the `n-i`th node, the slow pointer will be at the `n-i`th node as it is `i` nodes behind the fast node as established earlier.  
  
#### Conclusion
The time complexity is $O(n)$ where $n$ is the number of nodes in the linked list. The space complexity is $O(1)$, as requested by the follow-up question.  
  

