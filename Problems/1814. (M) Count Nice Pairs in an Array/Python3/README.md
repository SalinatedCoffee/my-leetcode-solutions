## 1814. (M) Count Nice Pairs in an Array

### `TLE.py`
The brute-force approach is to simply try evaluating the equality for every possible pair of integers in `nums`. Unfortunately, there is no simple formula that we can use to reverse the digits of an integer, and so we must do this manually by defining a function `def(k)` that reverses `k` using modulo operations and integer division. We then simply use a nested `for` loop to evaluate the equality, incrementing `ret` by `1` whenever it evaluates to `True`. Once the loops exit, we simply return `ret % mod` (where `mod == 10**9 + 1`).  

#### Conclusion
This implementation has a time complexity of $O(n^2)$ where $n$ is the length of `nums`. Reversing an integer takes logarithmic time with respect to the size of the integer which is technically unbound in Python. Nevertheless, we will consider it as $O(1)$ since other languages do limit the size of integers. The space complexity is $O(1)$.  
  

### `solution.py`
The previous attempt will result in TLE, and so we will need to find a way to speed it up. We immediately know that we can optimize the number of reversals being performed, as the previous implementation reverses the same integer multiple times. We also want to avoid evaluating the equation for every possible pair of integers in `nums`. Examining the equality `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])`, we can rearrange this expression so that each 'variable' is grouped nicely on each side. Using the rearranged equation `nums[i] - rev(nums[i]) = nums[j] - rev(nums[j])`, we can now compute `nums[i] - rev(nums[i])` for every integer in `nums` and simply *count* the number of integers that have the same computed value. That is, if `nums[i] - rev(nums[i]) == 14`, `nums[i]` forms a 'nice' pair with all other integers `nums[j]` where `nums[j] - rev(nums[j])` also evaluates to `14`.  
Initializing a `Counter` `diff`, we compute `nums[i] - rev(nums[i])` for all integers in `nums`. Using the evaluated value as the key, we increment the corresponding value in `diff` by `1`. We now have the number of integers that evaluate to the same values. The number of pairs that can be formed from $k$ integers that evaluated to the same value is $_kC_2$, for which Python conveniently provides the built in function `comb()` in the `math` module. Iterating over all *values* of `diff` then, we simply compute the number of possible pairs and add it to `ret`. Once this step is complete, we can finally return `ret % mod`.  

#### Conclusion
This solution has a time complexity of $O(n)$. `nums` is iterated over once, and as mentioned previously, we consider the reversing operation as having a time complexity of $O(1)$. `diff` can contain at most $n$ values, and as such the counting step can also take $O(n)$ time to run. The space complexity is $O(n)$, due to use of `diff`.  
  

