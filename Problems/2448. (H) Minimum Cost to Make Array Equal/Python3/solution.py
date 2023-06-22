class Solution:
  def minCost(self, nums: List[int], cost: List[int]) -> int:
    # prefix sums

    ncost_sorted = sorted(zip(nums, cost))
    n = len(nums)
    
    # generate prefix sums of costs
    # ps_cost[i] is prefix sum including cost of ncost_sorted[i]
    ps_cost = [0] * n
    ps_cost[0] = ncost_sorted[0][1]
    for i in range(1, n):
      ps_cost[i] = ps_cost[i-1] + ncost_sorted[i][1]

    # compute total cost of changing all numbers to first
    tot_cost = 0
    for i in range(n):
      tot_cost += ncost_sorted[i][1] * (ncost_sorted[i][0] - ncost_sorted[0][0])

    # compute minimum cost across all possible targets
    ret = tot_cost
    for i in range(1, n):
      diff = ncost_sorted[i][0] - ncost_sorted[i-1][0]
      tot_cost += ps_cost[i-1] * diff
      tot_cost -= (ps_cost[-1] - ps_cost[i-1]) * diff
      ret = min(ret, tot_cost)

    return ret

