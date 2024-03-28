class Solution:
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    # sliding window

    n = len(nums)
    ret = 0
    l, prod = 0, 1
    for i in range(n):
      prod *= nums[i]
      while l < i and prod >= k:
        prod //= nums[l]
        l += 1
      if prod < k:
        ret += i - l + 1

    return ret

