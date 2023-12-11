## 1287. (E) Element Appearing More Than 25% In Sorted Array

### `solution.py`
As the input size is relatively small, we can get away with taking the brute force approach by simply counting the frequency of each of the values in `arr`. Instead of counting the items manually we can use Python's built in counters to do the counting for us. We then iterate over each key-value pair and immediately return when a number has a frequency that is larger than `len(arr) / 4`.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the length of `arr`. Counting each element in `arr` takes $O(n)$ time, and the dictionary used by the counter will also use $O(n)$ memory.  
  


### `solution_2.py`
We can also implement a sliding window based solution, where we only allow identical elements inside a window. Iterating along `arr`, we add the current number to the window. If the number is different than the other numbers in the window we check whether the window is larger than 25% of `arr`. If so, we immediately return the number in the window. If not, we simply contract the window by removing all items previously contained in the window.  

#### Conclusion
The time complexity of this solution is $O(n)$, as we iterate over `arr` exactly once. The space complexity is $O(1)$.  
  


### `solution_3.py`
Because `arr` is sorted, and a answer is guaranteed to exist, a binary search based solution is also a valid approach. If we partition `arr` into 4 quarters, and take the 8 elements at each end of the partitions, the answer **must** be one of these 8 elements. We need to count the frequencies of each value to verify, and we can use binary search to do so. Python's `bisect` module does just that, where `bisect.bisect_left()` can be used to find the index of the first occurance and `bisect.bisect_right()` to find the last. If there are more occurances than `len(arr) / 4`, we can immediately return that value.  

#### Conclusion
This solution has a time complexity of $O(\log n)$. We select 8 candidates from `arr` and run binary search on `arr` twice for each candidate. A binary search on `arr` takes $O(\log n)$ time, and thus the overall time complexity is $O(\log n)$. The space complexity is $O(1)$.  
  

