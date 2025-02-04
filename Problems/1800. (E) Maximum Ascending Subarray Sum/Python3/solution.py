class Solution:
  def maxAscendingSum(self, nums: List[int]) -> int:
    # brute force

    n = len(nums)
    tot = nums[0]
    res = tot
    for i in range(1, n):
      if nums[i-1] < nums[i]:
        tot += nums[i]
      else:
        tot = nums[i]
      res = max(res, tot)

    return res

