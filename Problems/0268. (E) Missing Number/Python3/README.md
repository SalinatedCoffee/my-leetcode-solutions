## 268. (E) Missing Number

### `solution.py`
There are 2 facts about `nums` that we can take for granted. One is that `nums` is a list of unique integers in the range `[0, n]`, and another is that `nums` is missing a single value within the same range. Combining these facts we can say that `len(nums) == n` since `n` is 0-indexed. We can also say that `sum(nums) + m == n*(n+1)//2`, where `m` is the missing integer. `sum(nums)` can be computed in linear time, and computing the RHS is trivial. Rearranging, we get `m = n*(n+1)//2 - sum(nums)`, the value of which we can directly return.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
For languages that have fixed-sized integers(which is... pretty much all languages other than Python) `sum(nums)` may cause integer overflow. To avoid this, we can compute the XOR sum of `nums` instead, and XOR that value to the XOR sum up to `n`.  

