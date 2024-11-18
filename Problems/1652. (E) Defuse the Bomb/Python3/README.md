## 1652. (E) Defuse the Bomb

### `solution.py`
Given the circular array `code` and integer `k`, we are asked to return a list of sums of `k`-long subarrays in `code`. The subarray sums should be calculated differently depending on the value of `k`:  

- If `k < 0`, the `i`th element of the list of subarray sums should be the sum of `abs(k)` elements that come before `code[i]`.  
- If `k == 0`, all subarray sums should be `0`.  
- If `k > 0`, the `i`th element of the list of subarray sums should be the sum of `k` elements that come after `code[i]`.  

Let `code = [1, 2, 3, 4]` and `k = -2`, for example. The first element of the list of subarray sums `res` is the sum of the two elements that come before `code[0]`, which is `code[3] + code[2] == 4 + 3 == 7`. `res[1]` would be `code[0] + code[3] == 1 + 4 == 5`, and so on. If `k` was `2` instead, the value of `res[0]` would be `code[1] + code[2]`.  
As is usually the case with circular arrays, we can utilize the modulo operator to wrap the index around the end of the array as we iterate over it(Python supports negative indexes which are also a valid approach, but we will use modulo operations to keep the algorithm more portable across different languages). Because `code` is circular, there are `len(code)` subarrays of length `abs(k)` that must be examined - regardless of the sign of `k`. The only thing that changes with the sign of `k` is the location where the sum is saved within the list of subarray sums. For the subarray `code[0:abs(k)]`, the sum of this subarray should be stored as the `len(code) - 1`th element(1-indexed) in the list of subarray sums if `k` is positive, and `abs(k)` if `k` is negative. Once the position of the initial subarray sum has been determined, we can simply increment it in the same direction as the sliding window.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `code`. Because we use a sliding window to compute the sum of each `k`-length subarray of `code`, evaluating the sum of a single subarray takes $O(1)$ time to complete. As there are `n` such subarrays, the overall time complexity of this solution is $O(n)$, The space complexity is $O(1)$, excluding the list of subarray sums `res`.  
  

