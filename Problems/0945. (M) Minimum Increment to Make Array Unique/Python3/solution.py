class Solution:
  def minIncrementForUnique(self, nums: List[int]) -> int:
    # greedy

    n = len(nums)
    nums.sort()
    ret = 0
    for i in range(1, n):
      if nums[i] <= nums[i-1]:
        ret += nums[i-1] + 1 - nums[i]
        nums[i] = nums[i-1] + 1

    return ret

