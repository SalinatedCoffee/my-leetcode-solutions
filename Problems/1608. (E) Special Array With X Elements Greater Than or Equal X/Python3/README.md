## 1608. (E) Special Array With X Elements Greater Than or Equal X

### `solution.py`
While the problem description is slightly confusing, we know that the desired value will be in the interval `[0, len(nums)]`, if it exists. As `nums` is not sorted, we first sort it in ascending order to make it easier to work with. Because we are asked to find some integer `i` where there are *exactly* `i` elements in `nums` that are greater than or equal to `i`, we simply need to find a value where the index of the smallest value greater or equal to it subtracted from the length of `nums` equals the value itself. Since we have sorted `nums`, we can use binary search to search for the index of the appropriate element for each candidate value within the aforementioned range.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the length of `nums`. `nums` is first sorted before the binary search step, which takes $O(n\log n)$ time using Python's built in `list.sort()` method. After the sorting step, binary search is performed on `nums` $n$ times, with each pass taking $O(\log n)$ time to complete. Hence, the overall time complexity comes out to be $O(n\log n + n\log n) = O(n\log n)$. The space complexity is $O(n)$, due to the sorting step.  
  

