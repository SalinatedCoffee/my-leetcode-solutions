class Solution:
  def maxAdjacentDistance(self, nums: List[int]) -> int:

    n = len(nums)
    res = float('-inf')
    for i in range(n):
      res = max(res, abs(nums[i] - nums[i-1]))

    return res

