## 977. (E) Squares of a Sorted Array

### `solution.py`
We simply need to square each elements in `nums`, and then sort the resulting list before returning it. While `nums` is already sorted in ascending order, squaring negative values will make them positive, and thus we need to sort `nums` again once it has been squared.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the length of `nums`. Python's built in 'sorted' function takes $O(n\log n)$ time to sort an array of length $n$, hence the time complexity. The space complexity is $O(n)$, also due to the sorting step.  
  

### `solution_2.py`
We can make use of the fact that `nums` is already in ascending order to implement a solution that does not involve sorting(which is what the follow up question asks us to do). As mentioned in the previous solution, squaring a negative number makes it positive. Hence we are only interested in the *absolute* value of the elements in `nums`. Because `nums` is already in ascending order, it means that the largest squared value will be either the first or last elements squared. If we continue to move 'inwards' starting at both ends of `nums`, we will eventually end up with a list of squared values in decending order. Since we already know the size of the output list, we can simply iterate over an empty list in reverse while filling it with the larger of the two 'outward' values.  

#### Conclusion
This solution has a time complexity of $O(n)$. We iterate over the return list `ret` once, and comparing `nums[l]` and `nums[r]` takes constant time. Thus the overall time complexity comes out to be $O(n)$. The space complexity is $O(1)$, excluding the memory used by the output array `ret`.  
  

