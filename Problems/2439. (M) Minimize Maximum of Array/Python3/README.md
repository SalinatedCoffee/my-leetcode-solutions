## 2439. (M) Minimize Maximum of Array

### `solution.py`
Given the problem constraints, we can greedily distribute a number among the elements on its left side. If we assume that the array only increases, we can trivially calculate the smallest possible maximum number by getting the ceiling of the sum divided by the number of elements. This can be generalized to any range from index `0` to `i`, where the sum becoming the prefix sum up to index `i` and the number of elements becoming `i+1`. However, the array is not guaranteed to be in ascending order. If `nums[i+1]` is smaller than `nums[i]`, we should not 'move' the value of `nums[i+1]` since it would increase the deviation between numbers. The prefix sum however is always increasing, as well as the minimum max. number. Thus we choose the *larger* number between the current minimum max. number and the computed min. max. number at some index `i`.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

