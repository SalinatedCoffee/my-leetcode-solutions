## 347. (M) Top K Frequent Elements

### `solution.py`
The $O(n\log n)$ is trivial as we can simply create a dictionary mapping values to their frequency and return the slice of the list sorted by frequency.  

#### Conclusion
This solution runs in $O(n\log n)$ time where $n$ is the length of `nums`. `heapq.nlargest()` takes $O(n\log n)$ time to run since it generates a heap in the background. The space complexity is $O(n+n)$.  
  

