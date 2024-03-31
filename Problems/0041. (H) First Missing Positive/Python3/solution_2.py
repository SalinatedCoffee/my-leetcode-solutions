class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    # cycle sort
    
    n = len(nums)
    i = 0
    # place positive integers into their appropriate location in nums
    while i < n:
      idx = nums[i]-1
      if 0 < nums[i] <= n and nums[i] != nums[idx]:
        nums[i], nums[idx] = nums[idx], nums[i]
      else:
        i += 1

    # scan sorted nums for missing positive integer
    for i in range(n):
      if nums[i] != i+1:
        return i+1

    return n+1

