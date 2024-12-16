## 2762. (M) Continuous Subarrays

### `solution.py`
An array is considered to be 'continuous' when the difference between the largest and smallest elements of the array is less than or equal to `2`. Given the list of integers `nums`, we are asked to determine the total number of continuous subarrays in the list. First off, we can immediately see that a continuous subarray can contain at most 3 distinct elements. Because of this, we can take a sliding window approach as evaluating the validity of a window will take constant time. The frequency of each unique value in the current window will be stored in a dictionary. As the window is incrementally expanded towards the right, we check the dictionary to determine the difference between the largest and smallest values. Whenever the value exceeds `2`, we incrementally contract the window from the left until it becomes valid again. For each valid window, we know that there are `i` suffixes(valid subarrays that end with the last element in the current window) if the window is `i` elements long. Since we are asked to return the *total* number of valid subarrays in `nums`, we add `i` to the total counter before expanding the window.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. Sliding a variable length window over `nums` takes $O(n)$ time, and each window requires only $O(1)$ time to evaluate. The space complexity is $O(1)$, as the dictionary `window` can at most contain 4 key-value pairs.  
  

