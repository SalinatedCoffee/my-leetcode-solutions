class Solution:
  def waysToSplitArray(self, nums: List[int]) -> int:
    # prefix sum

    n = len(nums)
    tot = sum(nums)
    pre, res = 0, 0
    for i in range(n-1):
      pre += nums[i]
      if tot - 2*pre <= 0:
        res += 1

    return res

