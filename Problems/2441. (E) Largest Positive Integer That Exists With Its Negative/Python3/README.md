## 2441. (E) Largest Positive Integer That Exists With Its Negative

### `solution.py`
The brute force solution is to find a match for all elements in `nums`, returning the largest positive value that has a matching negative value. This approach however, has a quadratic time complexity as we have to scan the entirety of `nums` for each element. We can do much better by sorting `nums` and attempting to match the values at the extremities. After sorting `nums` in ascending order, we declare 2 pointers `l` and `h`, where the former points to the negative element being examined and the latter the positive. These pointers are initialized to `0` and `len(nums)-1` respectively. Then, while `l < h`, `nums[l] < 0`, and `nums[h] > 0`, we attempt to match `nums[l]` and `nums[h]`. If the two values sum to `0` they are a matching pair, and because we are examining a sorted list moving from the outside towards the inside, it is guaranteed that this pair has the largest absolute value within `nums`. Thus, we can simply return the value of `nums[h]`. Otherwise, we need to determine which pointer to advance by comparing the absolute value of the two values. If `nums[l]` is larger, we should try comparing `nums[h]` with the next negative value with a smaller absolute value than `nums[l]` which is simply `nums[l+1]`, and vice versa. If the while loop exits without returning, then `nums` contains no matching pairs, and we return `-1` as requested by the problem.  

#### Conclusion
The solution has a time complexity of $O(n\log n)$, where $n$ is the length of `nums`. Sorting `nums` using Python's built-in sort takes $O(n\log n)$ time, and the following iteration over the sorted list takes $O(n)$ time. The space complexity is $O(n)$ due to the sorting step.  
  

