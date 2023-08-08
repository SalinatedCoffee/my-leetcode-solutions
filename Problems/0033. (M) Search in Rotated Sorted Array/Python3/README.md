## 33. (M) Search in Rotated Sorted Array

### `solution.py`
A straightforward solution would be to simply 'split' `nums` about the pivot, which yields two sorted lists. It would take 3 binary search passes, but the solution would still be within the $O(\log n)$ time complexity limit. However, we can do it in 2 passes by realizing that we can convert between `nums` indices and un-pivoted indices if we know where the pivot is.  
The pivot in the rotated array can also be described as the first (leftmost) element in `nums` that is smaller than the last element in `nums`. Thus given some range bounded by `l` and `h`, and the middle element `m`, if `nums[m] < nums[-1]` we know that there still may be values smaller than `nums[m]` that are also smaller than `nums[-1]` in the left half of the range `[l, h]`. Now that we know which half to choose at every iteration we can use binary search to identify the index of the pivot.  
Given the pivot then, we want to shift the index in such a way that it becomes `0`. We can shift it to the right, by `len(nums) - pivot` and then take the modulo of `len(nums)`. So the conversion formula would be `(i + (len(nums) - pivot)) % len(nums)`. Verifying this against the first example given in the problem, `nums = [4,5,6,7,0,1,2]`, we have `len(nums) = 7` and `pivot = 4`. If we were to convert the index of `1`, we would have `(5 + (7 - 4)) % 7 = 8 % 7 = 1`, which is indeed correct.  
Using this conversion formula, we can now convert the original `nums` indices to the proper sorted ones, which in turn allows us to perform regular binary search for `target`. The range of the initial search space is `0` up to `len(nums) - 1`. For the middle element `m`, we know that it is in the pre-pivoted index domain. Thus we need to convert it back into the `nums` domain, which we can do with the expression `(m - (len(nums) - pivot) + len(nums)) % len(nums)`. Now we know which index in `nums` contains the middle element of the split, and so we can carry on performing our binary search.  
If the binary search exits without finding `target`, it means that `target` does not exist within `nums`, and we return `-1`.  

#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is the length of `nums`. We perform 2 passes of binary search on the entierety of `nums`, which takes $O(\log n)$ time per 1 pass. The space complexity is $O(1)$.  
  

### `solution_2.py`
A 1 pass solution is also possible. Binary search is based on the predicate that the array is already sorted. If the array is pivoted like this problem, it means that if we split it into two subarrays one of them is guaranteed to contain the pivot. The array that does *not* contain the pivot is guaranteed to be sorted, and thus we can trivially check whether a number exists in that array or not.  
Say that `nums` is indeed pivoted, and we split it into two halves of equal length. We have already established that one array must contain the pivot. Turning our attention to the array that does not contain the pivot then, we can check whether that array contains `target` or not. If it does, we should obviously discard the array that contains the pivot. Otherwise, we discard the array that *does not* contain the pivot. Like the first solution, if the search exits without finding `target`, we simply return `-1`.  

#### Conclusion
Like the first solution, this solution has a time complexity of $O(\log n)$ and a space complexity of $O(1)$.  
  

