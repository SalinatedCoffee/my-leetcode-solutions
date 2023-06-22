## 2448. (H) Minimum Cost to Make Array Equal

### `TLE.py`
It is always optimal to select a 'target' that already exists in `nums`, and so we can simply try a brute force solution. If we choose a target and some other number, the cost to make the other number equal to the target is simply the absolute difference between the two values multiplied by the cost of the other number. With this method, we can compute the total cost of shifting all values to the target, which we perform for all possible targets in `nums` to find the minimum possible sum.  

#### Conclusion
The time complexity is $O(n^2)$, where $n$ is the length of `nums`. For each value in `nums`, we compute the total cost of shifting all values in `nums` to that value, which takes $O(n)$ time. The space complexity is $O(1)$.  
  

### `solution.py`
The first approach takes quadratic time, which was obviously not fast enough for it to be accepted as a correct solution. Can we somehow reduce the cost-computing step to sublinear time?  
Going back to the beginning, we know that the total cost of shifting a value to a target value is the absolute difference of the two values multiplied by the cost of the original value. This is because one operation consists of either increasing or decreasing a value by `1`, and costs the corresponding amount specified in the list `cost`. Because the value change per operation is a fixed amount, we can 'batch' these operations for multiple values instead of evaluating the total cost for each value individually. For example, if `nums = [1, 1, 3]` and `cost = [1, 3, 4]`, the total cost of shifting the first two values to `3` is simply the sum of the costs of the two values times the difference between `1` and `3`. If we precompute the prefix sums for `cost`, we can perform this computation in constant time. Furthermore, if we sort the value-cost pair based on `nums` in ascending order (`ncost_sorted`), we can compute the total cost for each value efficiently by simply iterating over the sorted list of values. Say we initially compute the total cost to shift all values to the first value (which is also the smallest value in `nums`) in `ncost_sorted`, which we store in the variable `tot`. Let's now consider the total cost of shifting values to the next value, which is `ncost_sorted[1][0]`. Now we have to shift `ncost_sorted[0][0]` to `ncost_sorted[1][0]`, which is `ncost_sorted[1][0] - ncost_sorted[0][0]` multiplied by `ncost_sorted[0][1]`. On the other hand, we can now shift the values in `ncost_sorted[2:]` to `ncost_sorted[1][0]` using **less** operations, since `ncost_sorted[1][0]` is **larger** than `ncost_sorted[0][0]`(if they are equal, the total cost will not change). Since we have a precomputed list of prefix cost sums of `ncost_sorted`, this can also be computed in constant time in a similar fashion to how the cost increase was computed.  
Thus the algorithm will roughly take these steps:  
Initially sort both `nums` and `cost` based on `nums`  
Compute prefix sums on the costs in the sorted list `ncost_sorted`  
Compute the total cost of shifting all values to the first value in `ncost_sorted`  
Iterating over the values in `ncost_sorted`, compute the total cost to shift all values to each value by:  
	Computing the cost increase due to shifting the previous values  
	Computing the cost decrease due to the reduction in the number of performed operations shifting the subsequent values  
Return the smallest total cost among all values  
  
#### Conclusion
This solution will take $O(n\log n)$ time to run, where $n$ is the length of `nums`. The sorting step takes $O(n\log n)$ time, while precomputing prefix sums and the total cost computing step will take $O(n)$ time each. The space complexity is $O(n)$.  
  

	