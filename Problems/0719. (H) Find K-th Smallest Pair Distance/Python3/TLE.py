class Solution:
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    # binary search with brute force counting

    n = len(nums)

    # count number of pairs with distance less than or equal to d
    def count(d):
      ret = 0
      for i in range(n):
        for j in range(i+1, n):
          if abs(nums[i] - nums[j]) <= d:
            ret += 1

      return ret

    l, h = 0, max(nums) - min(nums)
    ret = h
    while l <= h:
      m = l + (h - l) // 2
      pairs = count(m)
      if pairs >= k:
        ret = m
        h = m - 1
      else:
        l = m + 1

    return ret

