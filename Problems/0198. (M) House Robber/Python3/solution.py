class Solution:
  def rob(self, nums: List[int]) -> int:
    # top-down dynamic programming (memoization)

    n = len(nums)

    @cache
    def recurse(i):
      # return maximum haul stealing from nums[:i] houses
      if i < 0:
        return 0
      return max(nums[i] + recurse(i-2), recurse(i-1))

    return recurse(n-1)

