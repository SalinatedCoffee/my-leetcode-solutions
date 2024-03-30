## 2958. (M) Length of Longest Subarray With at Most K Frequency

### `solution.py`
A brute force solution would involve evaluating all subarrays of `nums`. There are $O(n^2)$ subarrays of an array of length $n$, and evaluating each subarray will take $O(n)$ time. This is quite obviously, not optimal at all, and we must look for a different means in which to solve this problem. Thankfully, the problem is a quite straightforward sliding window problem which can be solved by supplimenting the approach with a dictionary.  
We iterate over `nums`, incrementally expanding the window every iteration. If at any point the newly added element invalidates the window, we simply keep contracting the window from the other side until it becomes valid again. To determine whether a window is valid or not, we can store the counts of each unique value within the window by using a dictionary.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. `nums` is effectively iterated over twice, with each iteration taking only $O(1)$ time to complete. The space complexity is also $O(n)$, due to the use of a dictionary to store information about the current window.  
  

