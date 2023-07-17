## 445. (M) Add Two Numbers II

### `solution.py`
When adding two numbers we typically do so starting with the least significant digits, as we need to account for the case where the sum of two digits is larger than 10(carry). In this problem however, the two numbers are given in the form of singly linked lists which prevents us from directly accessing the least significant digit. Taking into account the follow-up question which disallows us from reversing the given linked lists, there are a few approaches we can take to solve this problem. Here we will simply convert the two linked lists into integers, add them together, and then convert that number back into its linked list form. The first conversion step is trivial as we only need to traverse the list and shifting the sum 1 digit to the left (by multiplying it by 10) before adding the value of the current node. The second conversion step is a bit more involved as we need to know the number of digits in the integer beforehand. Again this can be solved in many different ways, but here we have taken the more mathematical approach where we compute the base 10 log of the value. Now we can generate the linked list form by doing the opposite of what we did for the first conversion, shifting the value 1 digit to the right until all digits have been processed.  

#### Conclusion
This solution takes $O(\text{max}(m, n))$ time to run, where $m$ and $n$ are the length of `l1` and `l2`, respectively. The space complexity is also $O(n)$, if the linked list being returned is taken into account.  
  

