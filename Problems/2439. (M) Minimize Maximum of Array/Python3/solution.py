class Solution:
  def minimizeArrayValue(self, nums: List[int]) -> int:
    # greedy

    ret = 0
    p_sum = 0
    for i in range(len(nums)):
      p_sum += nums[i]
      ret = max(ret, ceil(p_sum/(i+1)))

    return ret

