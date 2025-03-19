## 3191. (M) Minimum Operations to Make Binary Array Elements Equal to One I

### `solution.`
Given the binary array `nums`, we can select any 3 consecutive elements and flip them in a single operation. Our task is to return the minimum number of operations required to make all elements of `nums` `1`. If it is impossible to do so, we should return `-1`.  
We can immediately see that the first and last elements can only be flipped by flipping the (last) second and third elements as well. That is, if the first element is `0`, we must flip the first 3 elements as well WLOG. We can take a sliding window approach to this problem, sliding a window of length 3 starting from the left. If the first item in the window is `0`, we flip the entire window before moving on to the next element. Once all elements have been considered, we examine the last two element of `nums`. If any of them are still `0`, it is impossible to make all elements of `nums` `1` using the operation described. Otherwise, we simply return the total number of flips performed up to this point.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

