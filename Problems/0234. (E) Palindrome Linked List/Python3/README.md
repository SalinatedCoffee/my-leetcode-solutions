## 234. (E) Palindrome Linked List

### `solution.py`
The easy solution is to simply exploit the fact that reversing a palindrome results in the same sequence as the original palindrome. While iterating over the linked list, we add a record of each node in reverse using a deque(using a list and reversing it after would also work). We then iterate over the list again, while comparing each node's value to those stored in the deque. If the two values do not match at any point during the traversal, we can immediately return `False`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of the linked list having `head` as it's first node. The linked list is traversed twice, where each node takes $O(1)$ time to process. For memory, the values of the nodes in the linked list are stored in a deque, hence the overall space complexity of $O(n)$.  
  


### `solution_2.py`
The follow-up question asks us to implement a solution that runs in $O(n)$ time, using $O(1)$ memory. First off, know that this is impossible to achieve without modifying the given linked list, which is generally bad practice when writing code that will run in a production environment. We can implement a solution that runs within the required constraints by reversing half of the list, and then comparing the two halves. The pivot node is first found by using a pair of pointers, in which one traverses the list at a faster pace than the other. When the fast pointer reaches the end of the list, the slower pointer will be pointing to the middle node if the list has an odd length, and the first node of the second half otherwise. Starting at the middle node then, we iterate over the second half of the list while reversing it. Once the reversal completes, we simply iterate over the two halves while comparing the values of the two nodes.  

#### Conclusion
The time complexity of this solution is $O(n)$, and the space complexity is $O(1)$ as asked by the follow-up.  
One could argue that the modified list can be 'fixed' before returning, but it may be the case that the linked list is being accessed in a concurrent fashion, which would cause problems even if a 're-reversing' were to be implemented. The only way that one could prevent problems in such a setting would to make the solution atomic by using some form of mutex lock.  
  

