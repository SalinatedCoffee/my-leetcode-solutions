class Solution:
  def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
    # binary search on sorted list

    n = len(nums)
    nums.sort()

    res = 0
    for i in range(n):
      # find index of...
      #   ...largest element that would be less than lower after adding nums[i]
      l = bisect_left(nums, lower-nums[i], i+1, n)
      #   ...largest element that would be less than upper + 1 after adding nums[i]
      h = bisect_left(nums, upper-nums[i]+1, i+1, n)
      # add number of valid pairs including nums[i] to total sum
      res += h - l

    return res

