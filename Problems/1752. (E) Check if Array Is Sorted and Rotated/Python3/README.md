## 1752. (E) Check if Array Is Sorted and Rotated

### `solution.py`
Given the list of positive integers `nums`, we are asked to determine whether `nums` is a monotonically increasing list rotated an unspecified number of times. Since `nums` is small, we can trivially solve this problem by utilizing the fact that `nums` will be decreasing at at most 1 location if it is a rotated ascending array. Starting with the last element and first element of `nums`, we compare the pair and see whether they are in the correct order. If not, the flip a boolean flag to `True` to signify that a decrease has been detected. If the flag was already flipped, there are more than 1 decreasing adjacent pairs in `nums`, which means that `nums` is not a rotated ascending array.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

