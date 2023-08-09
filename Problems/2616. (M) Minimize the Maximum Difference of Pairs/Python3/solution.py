class Solution:
  def minimizeMax(self, nums: List[int], p: int) -> int:
    # greedy with binary search
    
    n = len(nums)
    nums_s = sorted(nums)

    def verify(t):
      # returns number of pairs with difference leq to t
      pairs = 0
      i = 0
      while i < n - 1:
        if nums_s[i+1] - nums_s[i] <= t:
          pairs += 1
          i += 2
        else:
          i += 1

      return pairs

    l, h = 0, nums_s[-1] - nums_s[0]
    while l < h:
      m = l + (h - l) // 2
      if verify(m) >= p:
        h = m
      else:
        l = m + 1
    
    return l

