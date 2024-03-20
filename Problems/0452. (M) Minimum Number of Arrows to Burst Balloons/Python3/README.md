## 452. (M) Minimum Number of Arrows to Burst Balloons

### `solution.py`
Personally I find the original problem description confusing - we don't really care about the y-coordinates so we can just 'squish' the y-coordinates and think about them as line segments along the x-axis. I really couldn't think of a way to reasonably solve this problem with the given list as-is, so I sorted the 2D list by the first item of each element(which is the default behavior in Python).  
What we then need to do is realize that we can solve this problem with a greedy algorithm. Consider this list of line segments: `[[0,5], [0,1], [3,5], [4,5]]`. To 'cut' these lines in few cuts as possible we can group the overlapping segments into two, `[[0,5], [0,1]]` and `[[3,5], [4,5]]`(`[0,5]` can be in the same group as `[4,5]` instead - it doesn't really matter in this example). Here we don't care about how many line segments we can put in one group, but rather how many *groups* we have to make to cut all lines. Case in point, cutting the second group first cuts 3 lines (`[0,5]`, `[3,5]`, and `[4,5]`) which is more than 2 if we cut the first group first. But we still have to make one more cut to cut all lines.  
Now that we know that when moving along a sorted list it is *always optimal* to group overlapping lines as soon as they are encountered, we can start implementing an algorithm as code. Iterating over a sorted list, for each line segment we check if the lower bound is between the overlapping region we've encountered so far. If it is we also check whether the upper bound of the current segment is also within the upper bound of the overlapping region, and if so use the upper bound of the current segment as the overlap bound instead. On the other hand if we encounter a segment that does not overlap with the previous lines we increment a counter('popping' the balloons in the previous group), then set the new overlap region as the current line segment.  
After the iteration is over, we need to check whether the last segment is included in a overlapping group since the counter is only updated whenever a non-overlapping line is encountered.  
  
#### Conclusion
The initial sorting runs in $O(n\log n)$ time and is the dominant factor (iteration takes linear time). In terms of memory, the solution uses $O(1)$ space since `list.sort()` performs an inplace sort.  
  
  
### `solution_2.py`
...but the first solution can be improved. Made better, faster, more concise. We have the technology.  
The key thing to note is that we don't have to keep track of the lower bound of the overlapping region. Since the list is sorted in ascending order based on the first element, the lower bound of the balloons will **never decrease**. Combine this with the fact that we're more interested in whenever we encounter a balloon that doesn't overlap we can safely disregard the lower bound and make changes to the solution accordingly.  
  
#### Conclusion
This solution has the same time complexity as the previous one; but in practice runs much faster thanks to a reduction in comparisons and variable assignments.
