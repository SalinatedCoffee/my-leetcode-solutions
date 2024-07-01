## 1550. (E) Three Consecutive Odds

### `solution.py`
Given a list of integers `arr`, we are asked to determine whether `arr` contains a subarray of length 3 that contains only odd values. We can trivially solve this through a sliding window based approach. One thing to consider for this problem is that `arr` has a minimum length of `1`, which can be trivially checked for.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `arr`. `arr` is iterated over exactly once, with each element taking $O(1)$ time to process. The space complexity is $O(1)$.  
  

