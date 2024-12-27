class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # top-down dynamic programming (memoization)

    n = len(nums)

    @cache
    # return number of sign combinations where
    # sum[idx:] + cur would equal target
    def recurse(idx, cur):
      if idx == n:
        return 1 if cur == target else 0
      res = recurse(idx+1, cur-nums[idx])
      res += recurse(idx+1, cur+nums[idx])
      return res

    return recurse(0, 0)

