class Solution:
  def minDifference(self, nums: List[int]) -> int:
    # greedy algorithm on sorted list

    n = len(nums)
    # handle edge cases
    if n <= 4:
      return 0

    nums.sort()
    ret = float('inf')
    for i in range(4):
      ret = min(ret, nums[n-1-i] - nums[3-i])

    return ret

