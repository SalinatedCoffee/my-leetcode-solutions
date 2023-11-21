class Solution:
  def countNicePairs(self, nums: List[int]) -> int:
    # brute force

    n = len(nums)
    mod = 10**9 + 7

    def rev(k):
      # given an integer k, reverse its digits and return the resulting integer
      ret = 0
      while k:
        ret *= 10
        d = k % 10
        ret += d
        k //= 10
      return ret
    
    ret = 0
    for i in range(n):
      for j in range(i+1, n):
        if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
          ret += 1
    
    return ret % mod

