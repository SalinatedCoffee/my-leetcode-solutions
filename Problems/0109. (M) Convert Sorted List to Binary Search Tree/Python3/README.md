## 109. (M) Convert Sorted List to Binary Search Tree

### `solution.py`
The basic idea of using recursion on halves is identical to [problem #108](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/), with the difference being that we are given a linked list instead of an array. We obviously cannot retrieve the nth node in constant time, and the best we can do is do it in linear time. In order to accomplish this by traversing the list only once, we can use two pointers traversing at different speeds. The slow pointer moves at a rate of 1 node per iteration while the fast pointer moves at 2. Then, whenever the fast pointer reaches the end of the list the slow pointer will be pointing at the node in the middle of the list. Using this method we can split the list in half and apply recursion on them as we did for problem #108.  
We also need to declare a helper function to avoid modifying the input list, as the provided function only accepts one parameter and thus there is no way of telling if we have reached the end of the list or not.  

#### Conclusion
This solution has a running time of $O(n\log n)$ where $n$ is the length of the linked list. The maximum recursion depth is $\log n$, and we traverse the entire list at each recursion depth. Consequently, the space complexity is $O(\log n)$.  
  

