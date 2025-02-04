class Solution:
  def check(self, nums: List[int]) -> bool:
    # brute force

    n = len(nums)
    if n == 1:
      return True

    discontinuity = False
    for i in range(n):
      if nums[i-1] > nums[i]:
        if discontinuity:
          return False
        else:
          discontinuity = True

    return True

