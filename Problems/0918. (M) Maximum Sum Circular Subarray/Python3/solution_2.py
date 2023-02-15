class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    # either array wraps around end or it does not
    # return max of 'normal' or wraparound subarray, whichever is larger
    # wraparound can be computed by finding minimum normal subarray

    # max 'normal' subarray sum
    normal_max = float('-inf')
    # min 'normal' subarray sum
    normal_min = float('inf')
    current_max = 0
    current_min = 0
    total = 0
    for i in range(len(nums)):
      current_max = max(current_max, 0) + nums[i]
      normal_max = max(normal_max, current_max)
      current_min = min(current_min, 0) + nums[i]
      normal_min = min(normal_min, current_min)
      total += nums[i]
    
    # 'normal' min is total, all elements are negative
    if normal_min == total:
      ret = normal_max
    # max wraparound subarray sum is 'normal' min subtracted from total sum
    else:
      ret = max(normal_max, total-normal_min)

    return ret

