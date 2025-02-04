class Solution:
  def longestMonotonicSubarray(self, nums: List[int]) -> int:
    # brute force

    n = len(nums)
    res = 1
    a, d = 1, 1
    for i in range(1, n):
      if nums[i-1] < nums[i]:
        a += 1
        res = max(res, a)
        d = 1
      elif nums[i-1] > nums[i]:
        d += 1
        res = max(res, d)
        a = 1
      else:
        a, d = 1, 1

    return res

