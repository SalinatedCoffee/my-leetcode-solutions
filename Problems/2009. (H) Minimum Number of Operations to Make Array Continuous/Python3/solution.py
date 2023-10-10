class Solution:
  def minOperations(self, nums: List[int]) -> int:
    # sliding window on sorted array
    
    n = len(nums)
    unums = sorted(set(nums))
    un = len(unums)

    l, r = 0, 0
    w = 0
    while r < un:
      while unums[r] - unums[l] > n - 1 and l < r:
        l += 1
      r += 1
      w = max(w, r - l)
    
    return n - w

