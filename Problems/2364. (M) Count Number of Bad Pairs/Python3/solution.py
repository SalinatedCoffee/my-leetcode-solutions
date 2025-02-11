class Solution:
  def countBadPairs(self, nums: List[int]) -> int:
    # counting using dictionary

    n = len(nums)
    res = 0
    # diff[i] is number of indices j where i == j - nums[j] evaluates to True
    #   for all j up to current
    diff = defaultdict(int)
    for i in range(n):
      d = i - nums[i]
      good = diff[d]
      res += i - good
      diff[d] = good + 1

    return res

