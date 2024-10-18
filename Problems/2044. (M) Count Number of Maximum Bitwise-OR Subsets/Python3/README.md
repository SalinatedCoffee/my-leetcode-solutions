## 2044. (M) Count Number of Maximum Bitwise-OR Subsets

### `solution.py`
Given the list of integers `nums`, we are asked to return the number of subsets of `nums` where the bitwise OR of their elements equal the maximum possible value. For example, consider the case where `nums = [1, 3]`. The maximum value achievable by bitwise ORing elements of `nums` is `3`, which can be easily verified in this trivial example. Enumerating the subsets of `nums` where ORing their elements results in a value of `3`, we get `[1, 3]` and `[3]`. Hence, we should be returning `2`.  
First off, we realize that the maximum value among the bitwise OR 'sum' of subsets of `nums` is simply the OR sum of all elements of `nums`. The problem now becomes counting the number of subsets that OR to this value. Because `nums` is very short(at most 16 elements) a brute force solution is an acceptable approach for this problem. For a particular subset, an element can fall under one of two cases; it can either belong to the subset, or not. This means that if we can verify whether the OR sum of a subset is equal to the maximum value in constant time, the problem can be solved in $O(2^n)$ time, which is reasonably small since the upper bound of $n$ is 16. The function `recurse` takes 2 arguments `i` and `cur`, with `i` being the index of the element of `nums` currently being considered and `cur` the bitwise OR sum of all previously selected elements. If `i == len(nums)`, there are no more elements left to consider. We compare `cur` and the maximum OR sum, and return `1` if they are equal or `0` otherwise. If `nums[i]` exists, we explore all possible choices by selecting the element(`recurse(i+1, nums[i] | cur)`) and ignoring it(`recurse(i+1, cur)`). The returned values are added together and returned.  

#### Conclusion
This solution has a time complexity of $O(2^n)$, where $n$ is the length of `nums`. The space complexity is $O(n)$, due to the recursion stack caused by `recurse`.  
  

