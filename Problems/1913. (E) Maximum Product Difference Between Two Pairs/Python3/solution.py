class Solution:
  def maxProductDifference(self, nums: List[int]) -> int:
    # greedy algorithm using sorting

    nums.sort()

    return nums[-1] * nums[-2] - nums[0] * nums[1]

