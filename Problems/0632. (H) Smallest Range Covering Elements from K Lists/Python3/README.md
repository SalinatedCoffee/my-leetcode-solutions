## 632. (H) Smallest Range Covering Elements from K Lists

### `solution.py`
Given the list of sorted lists of integers `nums`, we are asked to determine the smallest range which contains at least one element from every list within `nums`. If two ranges are of an identical size, the range that has the smaller starting point should be considered as the smaller range. Because we want the smallest possible range, the start/endpoint of the resulting range should also exist as elements in `nums` - which means that we can take a sliding window based approach to solve this problem. We first merge the lists within `nums` into a single list, flattening `nums` down 1 dimension. After sorting the merged list, we can use a sliding window to determine the smallest valid interval.  
`nums` is flattened into the 1D list `mg_nums`, which is sorted in ascending order afterwards. While flattening `nums`, we also need to remember to label each element with the index of the list in `nums` that it was a part of in order to determine the validity of a window during the sliding window step. We need to keep track of 4 things for the sliding window step; `freq`, the number of elements in the current window from each list in `nums`, `c`, the number of lists 'represented' by the current window, `l`, the index of the left side of the current window, and `i` and `j`, the current smallest valid range. We incrementally expand the window towards the right, updating `freq` in accordance to the newly added element. If the current window is valid we incrementally contract the window until it becomes invalid, updating the smallest range if possible before every contraction. Once the sliding window step completes, we return `i` and `j` inside a list.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the number of integers across all lists within `nums`. `nums` is flattened into a single list and is sorted shortly thereafter. This step requires $O(n\log n)$ time to complete using Python's built in sort. The sliding window step that follows completes in $O(n)$ time, bringing the overall time complexity to $O(n\log n)$. The space complexity is $O(n)$, due to the sorting step and the merged list `mg_nums`.  
  
