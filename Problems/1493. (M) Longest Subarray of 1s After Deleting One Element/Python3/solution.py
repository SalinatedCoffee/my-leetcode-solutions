class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    # dynamic programming (pre/suffix sums)

    n = len(nums)
    l, r = 0, n-1
    p, s = 0, 0
    prefix = [0] * n
    suffix = [0] * n
    for i in range(n):
      prefix[l] = p
      suffix[r] = s
      if nums[l] == 1:
        p += 1
      else:
        p = 0
      if nums[r] == 1:
        s += 1
      else:
        s = 0
      l += 1
      r -= 1
    if p == n:
      return n-1

    ret = 0
    for i in range(n):
      if not nums[i]:
        ret = max(ret, prefix[i] + suffix[i])

    return ret

