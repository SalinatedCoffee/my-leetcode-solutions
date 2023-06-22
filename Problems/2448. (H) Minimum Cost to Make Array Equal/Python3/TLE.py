class Solution:
  def minCost(self, nums: List[int], cost: List[int]) -> int:
    # brute force
    
    n = len(nums)
    ret = float('inf')
    for i in range(n):
      c_tot = 0
      for j in range(n):
        c_tot += abs(nums[i] - nums[j]) * cost[j]
      ret = min(ret, c_tot)

    return ret

