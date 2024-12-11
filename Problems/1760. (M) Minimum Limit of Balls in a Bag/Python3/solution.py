class Solution:
  def minimumSize(self, nums: List[int], maxOperations: int) -> int:
    # binary search

    # returns True if at most maxOperations operations can be performed
    # to divide bags such that each bag holds up to size balls
    def verify(size):
      ops = 0
      for num in nums:
        ops += ceil(num / size) - 1
        if ops > maxOperations:
          return False

      return True

    # perform binary search on minimum bag size
    l, h = 1, max(nums)
    while l < h:
      m = l + (h - l) // 2
      if verify(m):
        h = m
      else:
        l = m + 1

    return l

