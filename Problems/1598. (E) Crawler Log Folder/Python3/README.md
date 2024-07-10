## 1598. (E) Crawler Log Folder

### `solution.py`
Given a list of `cd` arguments `logs`, we are asked to return the number of directories that we would have to move upwards to reach the main directory(or `/`, the root directory). Since we are only asked to return the number of directories we need to move out of to reach the main directory, we can get away with using a single integer to keep track of the current depth relative to the root directory. Whenever a `../` is encountered we decrement `depth` by `1` if it is not already `0`. Otherwise, we increment `depth` by `1` as long as the command is not `./`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `logs`. All string comparisons are performed against strings of fixed size(`./` and `../`) and hence, evaluating a single command in `logs` takes $O(1)$ time. The space complexity is $O(1)$.  
  

