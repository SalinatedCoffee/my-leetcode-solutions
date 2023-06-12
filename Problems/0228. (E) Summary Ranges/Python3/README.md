## 0228. (E) Summary Ranges

### `solution.py`
In order to verify that a subarray is indeed continuous we must know all of the values in that subarray, and thus we need to iterate along the entirety of `nums`. We keep track of the first value of the hypothetical range and check values in the list sequentially until a 'gap' is detected. Then we do another check to see whether the range includes one or more values and append the appropriate string to the return list.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the length of `nums`, since `nums` is iterated over once and each iteration takes constant time to compute. The space complexity is $O(1)$.  
  

