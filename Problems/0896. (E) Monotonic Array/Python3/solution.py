class Solution:
  def isMonotonic(self, nums: List[int]) -> bool:

    # sanity check
    if len(nums) <= 2:
      return True

    n = len(nums)
    d = nums[1] - nums[0]
    s = d // abs(d) if d != 0 else 0
    for i in range(2, n):
      d = nums[i] - nums[i-1]
      if d == 0:
        continue
      if s == 0:
        s = d // abs(d)
      else:
        if s * d < 0:
          return False

    return True

