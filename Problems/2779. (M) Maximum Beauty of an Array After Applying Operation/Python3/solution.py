class Solution:
  def maximumBeauty(self, nums: List[int], k: int) -> int:
    # sliding window on sorted array

    n = len(nums)
    nums.sort()
    l, res = 0, 0
    for i in range(n):
      while l <= i and nums[i] - nums[l] > 2 * k:
        l += 1
      res = max(res, i - l + 1)

    return res

