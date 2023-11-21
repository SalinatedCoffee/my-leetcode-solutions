class Solution:
  def countNicePairs(self, nums: List[int]) -> int:
    # counting with dictionary

    n = len(nums)
    mod = 10**9 + 7

    def rev(k):
      ret = 0
      while k:
        ret = ret * 10 + k % 10
        k //= 10
      return ret
    
    ret = 0
    diff = Counter([i - rev(i) for i in nums])
    ret = sum([comb(i, 2) for i in diff.values()])
    
    return ret % mod

