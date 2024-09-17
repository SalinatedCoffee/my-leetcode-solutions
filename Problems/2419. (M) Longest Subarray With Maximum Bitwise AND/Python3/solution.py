class Solution:
  def longestSubarray(self, nums: List[int]) -> int:

    n = len(nums)
    tgt = max(nums)
    l, res = -1, 0
    for i in range(n):
      if nums[i] != tgt:
        l = i
      else:
        res = max(res, i - l)

    return res

