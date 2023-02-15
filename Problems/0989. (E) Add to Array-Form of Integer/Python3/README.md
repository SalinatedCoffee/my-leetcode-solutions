## 989. (E) Add to Array-form of Integer

### `solution.py`
This problem is just [problem #67 Add Binary](https://leetcode.com/problems/add-binary/) with a slight twist. We can use the same strategy, but using modulo operations on `k` as it is provided as an integer. Unfortunately, since both numbers are in base 10 we can't use bitwise operations to extract the first digit of `k`(though it doesn't really matter because `k % 10` will be performed 3 times at most).  

#### Conclusion
The solution runs in $O(n)$ time and space, where $n$ is equal to `max(len(num), len(str(k)))`. $O(n)$ time because we touch all digits in `num` and `k`; $O(n)$ space because the resulting list is either $n$ or $n+1$ (leftover carry after last addition) long.  
  

