class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    # greedy algorithm using prefix sum on sorted list

    n = len(nums)
    nums.sort()
    pre = sum(nums[:2])
    ret = -1
    for i in range(2, n):
      if nums[i] < pre:
        ret = max(ret, nums[i] + pre)
      pre += nums[i]

    return ret

