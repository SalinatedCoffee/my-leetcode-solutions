## 1508. (M) Range Sum of Sorted Subarray Sums

### `solution.py`
For the sorted list of subarray sums of `nums`, we are asked to return the sum of all elements from `left` up to `right`(1-indexed, inclusive). For example, if `nums = [1, 2, 3]` and `left = 2`, `right = 4`, the return value is `8`. The sorted list of subarray sums is `[1, 2, 3, 3, 5, 6]`, and thus the sum of the subarray starting at the `2`nd element and ending at the `4`th element is `2 + 3 + 3 = 8`. The easiest way to solve this problem is through brute force, where the sum of all subarrays are computed and then sorted.  

#### Conclusion
The time complexity of this solution is $O(n^2\log n^2)$, where $n$ is `n`. A array of length $n$ has $n(n+1)/2$ subarrays, and calculating the sum of one subarray takes $O(1)$ time because the sums are incrementally computed. This list of subarray sums is then sorted using Python's built-in sort, which requires $O(n^2\log n^2)$ time to perform on a list of length $O(n^2)$. The space complexity is $O(n^2)$, since the entire list of subarray sums are kept in memory.  
  

### `solution_2.py`
We can optimize the space complexity by a factor of $n$ by using a priority queue instead of taking the brute force approach. Because we only want the first `right` smallest subarray sums, we do not need to generate the entire list. A priority queue allows us to consider subarray sums in order of their value, which we can take advantage of to partially generate the list of subarray sums.  
The basic idea is that the priority queue is first populated by the starting element of each subarray, and are incrementally expanded towards the right in order of their value. A sum is annotated with the index of its last value in order to keep track of which element to add when the subarray is expanded. We first initialize the priority queue(heap) `sums` with tuples using the elements in `nums`. The first element of a tuple will be the sum of the subarray it represents, and the second element will be the index(0-indexed) of the last element in that subarray. We can now start computing the subarray sums by iterating from `1` to `right`. Because the sums are stored in a priority queue, the iteration variable is the position of the current sum in the sorted list of subarray sums. After popping an item off of the queue, we first check whether the sum belongs in the range specified by `left` and `right`. If it is, the current sum is added to the total sum `ret`. If not, the subarray is expanded to the right by `1` if possible and is added back into the priority queue. If it cannot be expanded, the subarray is simply discarded. Once all elements up to `right` have been examined, `ret` will contain the desired value.  

#### Conclusion
This solution has a time complexity of $O(n^2\log n)$. The priority queue can contain at most $n$ items at any point in time. Hence, modifications to the priority queue will always take $O(\log n)$ time to complete. These operations are performed a fixed number of times for each subarray sum, of which there are $O(n^2)$. Thus, the overall time complexity of this solution is $O(n^2\log n)$. The space complexity is $O(n)$, because of `sums`.  
  

