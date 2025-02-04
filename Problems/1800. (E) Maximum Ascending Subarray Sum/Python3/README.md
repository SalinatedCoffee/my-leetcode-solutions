## 1800. (E) Maximum Ascending Subarray Sum

### `solution.py`
Given the list of positive integers `nums`, we are asked to return the largest sum of a strictly increasing subarray of `nums`. As `nums` is tiny, we can simply iterate over it while greedily adding elements to the current increasing subarray whenever possible.  
We will keep track of the sum of the current ascending subarray in `tot`, which we initialize as the value of the first element of `nums`. `nums` is then iterated over starting from the second element. For each value in `nums`, we compare it with the previous value. If the current value is strictly greater than the previous one, we add the current value to the ascending subarray by adding it to `tot`, after which we update the largest observed sum `res` as necessary. Otherwise, the current element is now the first element of a new ascending subarray, which we reflect by assigning the value of the current element to `tot`. Once the entirety of `nums` has been examined, `res` will contain the largest observed subarray sum.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

