class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    # prefix sums with dictionaries

    n = len(nums)
    # sums[i] is leftmost index of end of subarray that 'sums' to i
    sums = {}
    ret = 0
    # if nums[i] == 1, increments by 1
    # otherwise, decrement by 1
    prefix_sum = 0
    for i in range(n):
      if prefix_sum in sums:
        ret = max(ret, i - sums[prefix_sum])
      else:
        sums[prefix_sum] = i
      prefix_sum += 1 if nums[i] else -1
    if prefix_sum in sums:
      ret = max(ret, n - sums[prefix_sum])

    return ret

