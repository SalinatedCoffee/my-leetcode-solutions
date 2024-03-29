## 0057. (M) Insert Interval

### `solution.py`
A rather simple solution is to just append the new interval to the interval list, sort the list by the lower bound of an interval, and then iterate through the list while merging overlapping intervals. The merge step comes directly from problem #56, [Merge Intervals](https://leetcode.com/problems/merge-intervals/). After the sort we know that the lower bound of the intervals monotonically increase as we move along the list. If we keep track of the previous interval, whenever the current interval's lower bound is smaller than the tracked interval's upper bound we know that there is an overlap. There can be two types of overlap here; the current interval extends beyond the tracked interval(e.g. `[2, 5]` and `[3, 8]`), and the opposite where the tracked interval is longer than the current one(e.g. `[2, 9]` and `[4, 6]`). Here, we take the upper bound of both intervals and simply choose the largest value.  

#### Conclusion
The solution runs in $O(n\log n)$ time where $n$ is the number of intervals since we perform an in-place sort at line 12. Consequently the space complexity is $O(1)$ ( $O(n)$ if we count `intervals` as occupied memory) since we don't use additional memory in a way that scales with the size of the given input.  
  
  
### `solution_2.py`
This solution takes a slightly different approach in that it merges overlaps on the fly while generating a new list. We know that all correct return lists consists of 3 sublists; a list that contains all intervals strictly smaller than the merged interval('lower'), a list that contains one merged interval, and a list that contains all intervals strictly larger than the merged interval('upper'). If we allow 'lower' and 'upper' to be empty lists we can account for edge cases where the new interval is smaller than all intervals and vice versa.  
We iterate over the given interval list and append intervals that do not overlap. If we encouter an overlap, we flip the `merge` flag to denote that a merge is in progress. When we arrive at the 'upper' portion of the interval list either a merge-in-progress or the new interval must be inserted (since we checked for `newInterval[1] < intervals[i][0]`). After the iteration we check `insert` to see whether an insertion has taken place and if not, simply append the new interval to the end of the return list(since no insertions across entire list means all intervals are strictly smaller than the new one).  
  
#### Conclusion
The time complexity for this solution is $O(n)$, since it iterates over `intervals` once. The space complexity is $O(1)$, if the returned list `ret` is not counted. 
  

### `solution_3.py`
The previous solution can be rewritten into a more streamlined implementation by logically 'partitioning' `intervals` into 3 parts and processing them seperately. This involves 3 separate while blocks, where the first processes non-overlapping intervals to the left of `newInterval`, the second intervals that overlap with `newInterval`, and the last processing non-overlapping intervals to the right of `newInterval`. Processing non-overlapping intervals is trivial, as we only need to append them to the return list as-is. For the overlapping intervals, we keep updating the interval boundries by using `min` and `max`, after which we append the single merged interval to the list. Once the entirety of `intervals` have been processed, we simply return the new list of intervals.  
  
#### Conclusion
The time and space complexity for this solution is identical as the previous solution.  
  