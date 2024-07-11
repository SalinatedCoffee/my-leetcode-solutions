## 25. (H) Reverse Nodes in k-Group

### `solution.py`
Given the head node of a singly linked list and an integer `k`, we are asked to reverse each group of `k` nodes and return the head of the modified list. The value of a node cannot be altered, and we are not allowed to create new nodes. If there are less than `k` nodes remaining, we are asked to leave them as-is. So if the linked list is `[1, 2, 3, 4, 5, 6, 7, 8]` and `k = 3`, the modified list would look like `[3, 2, 1, 6, 5, 4, 7, 8]`. Observe how the first 2 groups of `k` nodes are reversed, while the last group of `2` nodes are left untouched. We can take a two pointer approach for this problem, where the linked list between the two nodes being pointed to is reversed before moving onto the next section. After a section is reversed we need 4 references to reconnect it back to the linked list. We need a reference to the tail of the previous section, the head and tail of the reversed section, and the head of the next section. These can be trivially stored before a reversal is performed.  
We first start by checking whether `k == 1`. For some odd reason the problem constraints allows `k` to be `1`, which means that no nodes are reversed. In this case, we simply return `head`. Otherwise, we initialize two pointers `l` and `h`, with both of them initially pointing to the tail of the previous section. Since there is no previous section before a reversal has occurred, we add a sentinel node before `head` and have `l` and `h` point to it. We then enter a loop that first advances the high pointer by `k` nodes. If `h` is `None` after this step, there are less than `k` nodes in the remaining section, and we exit immediately by returning `sentinel.next`. Otherwise we store the relevant node references and start reversing the current section. Once the section has been reversed, we use the references stored before the reversal to relink the modified section back into the linked list.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the given linked list. The linked list is traversed exactly once, with each node being reversed at most once. Hence, the overall time complexity comes out to be $O(n)$. The space complexity is $O(1)$, as we only use a handful of fixed-size variables over the entire running time of the solution.  
  
