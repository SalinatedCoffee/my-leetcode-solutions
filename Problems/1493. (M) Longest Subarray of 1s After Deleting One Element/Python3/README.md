## 1493. (M) Longest Subarray of 1's After Deleting One Element

### `solution.py`
Because we are only allowed to remove one number from `nums`, we can think of this as 'gluing' two subarrays of `1`s together. At some value with index `i` in `nums`, if we know the length of the `1`-subarrays on either side of it we can easily compute the total length of the `1`-subarray we would get by deleting the value at index `i`. To achieve this we precompute the lengths of prefix and suffix `1`-subarrays in lists `prefix` and `suffix`. `prefix[i]` contains the length of the `1`-subarray in the range `nums[:i]` that ends at `nums[i-1]`, and `suffix[i]` contains the length of the `1`-subarray in the range `nums[i+1:]` that starts at `nums[i+1]`. Then at some element `i` in `nums`, the length of the `1`-subarray we would get by deleting the value `i` would simply be `prefix[i] + suffix[i]`.  
One edge case is when `nums` only contains `1`. A value **must** be deleted, so in this case the answer would be `len(nums)-1`. We can detect this during the precomputation step by checking if the prefix sum of the last element is equal to the length of `nums`.  

#### Conclusion
This solution has a time complexity of $O(3n) = O(n)$ where $n$ is the length of `nums`. The precomputation step populates `suffix` and `prefix` which are both $n$ long, after which we iterate over the entierety of `nums` exactly once. The space complexity is $O(2n) = O(n)$.  
  

### `solution_2.py`
While the previous solution is already at linear time complexity, we can reduce the constant component and the space complexity even further by taking a sliding window approach. While iterating along `nums` (with loop variable `i`), we also keep track of the index `l` where the window begins. Whenever the current number is a zero we increment the counter `zeros`, which represents the number of `0`s in the subarray `nums[l:i+1]`. If this counter exceeds `1`, the subarray is no longer valid and so we keep advancing `l` until there is once again only 1 zero in the subarray.  

#### Conclusion
The time complexity for this solution is $O(2n) = O(n)$. `nums` is explicitly iterated over once, and implicitly iterated over once again through the variable `l`. The space complexity is $O(1)$.  
  