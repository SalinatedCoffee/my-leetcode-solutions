class Solution:
  def specialArray(self, nums: List[int]) -> int:
    # binary search on sorted list

    n = len(nums)
    nums.sort()
    # for all possible candidate values
    for i in range(1, n+1):
      # perform binary search to find index of first value leq to candidate
      l, h = 0, n-1
      last = n
      while l <= h:
        m = (l + h) // 2
        if nums[m] >= i:
          last = m
          h = m - 1
        else:
          l = m + 1
      if n - last == i:
        return i

    return -1

