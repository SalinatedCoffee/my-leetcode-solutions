class Solution:
  def findMaxK(self, nums: List[int]) -> int:
    # two pointers on sorted list

    l, h = 0, len(nums)-1
    nums.sort()
    while l < h and nums[l] < 0 and 0 < nums[h]:
      if nums[l] + nums[h] == 0:
        return nums[h]
      if nums[l] + nums[h] > 0:
        h -= 1
      else:
        l += 1

    return -1

