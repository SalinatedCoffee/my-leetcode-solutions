## 2134. (M) Minimum Swaps to Group All 1's Together II

### `solution.py`
`nums` is a list of integers and only contains `0`s and `1`s. It is also a circular array in that the next value of `nums[len(nums)-1]` is `nums[0]`(and vice versa). Given these conditions, we are asked to determine the minimum number of swaps to collect all `1`s into a contiguous subarray. Because `nums` is circular, collections such as `[1, 1, 0, 0, 0, 0, 1]` are also valid.  
There are two things we should consider. Firstly, we can collect the `1`s anywhere in `nums`. Secondly, we cannot modify the elements of `nums` which means that after collecting the `1`s into a single subarray the length of that subarray will always be equal to the number of `1`s in `nums`. These properties tell us that the problem can be solved through a sliding window approach. Through the first property, we know that the length of the window should be the number of `1`s in `nums`. Through the second property, we know that the number of `0`s in the window is the number of swaps that have to be performed to fill the window with `1`s. The array being circular can easily be handled by modulo operations, turning the problem into a trivial sliding window problem.  
We first initialize the window covering `nums[:w]`, where `w` is the number of `1`s(and thus the length of the sliding window) in `nums`. After counting the number of `0`s in the first window, we start sliding it across `nums`. The number of zeros is changed appropriately depending on whether the evicted/added element is equal to `0`. Because the array is circular, the right end of the window needs to be pushed beyond the end of `nums` by exactly `w` which can be handled by the iteration variable mod `len(nums)` as mentioned earlier. Once the iteration exits the smallest zero count among all window positions is the desired answer, which we can return directly.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. Counting the number of `1`s in `nums` takes $O(n)$ time, as well as the sliding window step that follows. The space complexity is also $O(n)$, due to the use of `filter`.  
  

