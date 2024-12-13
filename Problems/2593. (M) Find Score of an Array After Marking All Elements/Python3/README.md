## 2593. (M) Find Score of an Array After Marking All Elements

### `solution.py`
Given the list of positive integers `nums`, we are asked to determine the resulting score after running the following steps to completion:  

- The initial score is `0`.  
- Select the smallest integer that has not been **marked**. If there are multiple such integers, select the one that appears earliest in `nums`(element with smallest index).  
- Add the value of the selected integer to the score.  
- **Mark** the selected integer and its two adjacent elements.  
- Stop when all elements have been **marked**.  

We can easily implement an algorithm according to the steps described by using a heap and a set. The heap will contain the elements of `nums` that are yet to be examined, represented by a tuple containing the value and index of each element. The set will keep track of the indices of marked elements. While the heap is not empty, we pop an item off of it and consult the set to determine whether it has been marked or not. If not, we add the value to the score and mark the neighbors of the item. Once the heap is empty, we can return the accumulated score directly.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the length of `nums`. Initializing the heap with the contents of `nums`, as well as popping all elements from the heap are both $O(n\log n)$ time operations. The space complexity is $O(n)$, due to the heap.  
  

### `solution_2.py`
We can implement a more efficient solution by exploiting a property of the selection step. Say that the element `nums[i]` is smaller than the previous element `nums[i-1]`. Because we should be selecting the smallest integer during each step, we know that `nums[i]` will be chosen over `nums[i-1]` if both elements have not been marked. Moving on to the element `nums[i+1]`, there are 3 cases that we should be considering. The first case is when `nums[i+1]` is larger than `nums[i]`. Again assuming that all three elements are not marked, we know that `nums[i]` will be chosen. Next is when `nums[i]` and `nums[i+1]` are equal. Since the steps require us to use the index as the tiebreaker, `nums[i]` will be chosen in this case as well. Lastly, we consider the case where `nums[i+1]` is smaller than `nums[i]`. In this case, `nums[i+1]` will be selected in favor of `nums[i]`. Naturally, `nums[i]` will now be marked as a consequence of `nums[i+1]` being selected, which in turn means that `nums[i-1]` will now be selected.  
Putting everything together, we can see that we would want to keep track of the *continuous* strictly decreasing subarray that ends with the current element as we iterate over `nums`. Whenever it is determined that this subarray will no longer be strictly decreasing by appending the current element, we traverse the subarray while adding the values of the appropriate elements to the score. The subarray is then reset, and the current element is added to it. This algorithm can be implemented by using a decreasing monotonic stack, modified to empty the stack whenever the current element is larger than the item on top. Once all elements of `nums` have been examined, we empty the stack one last time to update the score before returning the resulting value.  

#### Conclusion
This solution has a time complexity of $O(n)$. `nums` is iterated over exactly once, with each element taking $O(1)$ time to process. The space complexity is also $O(n)$, due to the stack.  
