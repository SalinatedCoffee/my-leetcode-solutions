class Solution:
  def numSubseq(self, nums: List[int], target: int) -> int:
    # sort with two pointers

    nums.sort()
    l, h = 0, len(nums)-1
    ret = 0
    mod = 10**9 + 7
    while l <= h:
      if nums[l] + nums[h] > target:
        h -= 1
      else:
        ret += 2**(h-l)
        ret %= mod
        l += 1

    return ret

