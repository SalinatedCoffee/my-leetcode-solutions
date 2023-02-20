class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    # dp with memoization of min/max prods, based on kadane's algorithm

    overall_max = nums[0]
    running_max = nums[0]
    running_min = nums[0]
    for i in range(1, len(nums)):
      # get product of current with previous running max/min prod
      prod_max = nums[i] * running_max
      prod_min = nums[i] * running_min
      # select min/max between current, prod min/max
      running_max = max(nums[i], prod_max, prod_min)
      running_min = min(nums[i], prod_max, prod_min)
      # update overall maximum accordingly
      overall_max = max(overall_max, running_max)

    return overall_max

