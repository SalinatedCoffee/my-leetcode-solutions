## 45. (M) Jump Game II

### `solution.py`
Intuition tells us that if we know the minimum number of jumps to reach `i`, we can also compute the minimum jumps for all positions in the range `[i, i+nums[i]]`. We initialize a list `dp`, where `dp[i]` contains the minimum number of jumps required to reach index `i`. Iterating through `nums` then, we first check whether we can reach `nums[-1]` at the current index. If not we update elements in `dp[i:i+nums[i]+1]` accordingly, based on the value of `dp[i]`.  
  
#### Conclusion
The time complexity for this solution is $O(n^2)$ where $n$ is the length of `nums`. While the nested `for` loop on line 18 does [scale with the *value*](https://en.wikipedia.org/wiki/Pseudo-polynomial_time) of `nums[i]` and not the size of `nums`, the `if` on line 15 implicitly guarantees that the nested loop only ever goes up to `len(nums)-2`.  
The space complexity is $O(n)$.  
  

### `solution_2.py`
The first solution just barely runs within the accepted time limit. Upon further inspection we can see that it performs a lot of redundant computation. For example given `nums = [3,2,2,2,1]` it will compute `dp[1]` and `dp[2]` multiple times, which is clearly not necessary. To avoid this we need to take a different approach. Instead of computing the minimum number of jumps for all positions we can incrementally build up to the correct answer by thinking in ranges. Say we start at index `0`. If `nums[0]` is `3`, the furthest index we can reach is `3`, so we iterate along `nums` until `nums[3]`. Along the way, we encounter `nums[1] = 3`, `nums[2] = 1`, and `nums[3] = 2`. We can think of these positions as one 'block' since they can all be reached by a single jump from index `0`. The farthest index we can reach from this block then, is `max(1+3,2+1,3+2)` which is equal to `5`. Now the next 'block' becomes `nums[4:5+1]` because `5` was the farthest index we could reach by a single jump from the previous block. We can repeat this process until we reach `nums[-2]` while incrementing a counter whenever we make a jump to the next block, and when we exit the loop the counter will contain the minimum number of jumps required to reach `nums[-1]`. We iterate up to `range(len(nums)-1)`(`nums[-2]`) since the *last element* is the goal, and we know that we can reach `nums[-1]` if we consider elements up to `nums[-2]` because it is guaranteed that `nums[-1]` is reachable.  
  
#### Conclusion
This solution runs in $O(n)$ time and uses $O(1)$ space.  
Notice how both solutions are similar to BFS. The second solution performs much better by not revisiting any 'nodes'.  
  
