class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    # greedy algorithm on sorted list

    n = len(nums)
    nums.sort()
    for i in range(n-3, -1, -1):
      if nums[i] + nums[i+1] > nums[i+2]:
        return sum(nums[i:i+3])

    return 0

