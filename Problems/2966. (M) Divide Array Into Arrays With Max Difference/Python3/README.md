## 2966. (M) Divide Array Into Arrays With Max Difference

### `solution.py`
Immediately we can see that we should be partitioning `nums` as optimally as possible. For example, consider the input `nums = [1, 2, 3, 4, 5, 6]` and `k = 3`. `[[1, 2, 4], [3, 5, 6]]` is a valid partition for the given values, but not the most optimal. The most optimal partitioning is `[[1, 2, 3], [4, 5, 6]]` since the max difference of each partition is `2` instead of `3` for the non-optimal answer. This is a somewhat contrived example, but we want to be optimal in our partitioning so that other partitions have a greater chance of being valid. The easiest way that this can be achieved is by first sorting `nums`, and then sequentially partitioning it as described in the problem. If at any point of the partitioning we come across a partition that is considered invalid, we return `[]` as there is no valid partition of `nums`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `nums`. `nums` is first sorted, which takes $O(n\log n)$ using Python's built in sort. The actual partitioning takes $O(n)$ time. The space complexity is $O(n)$, also due to the sorting step.  
  

