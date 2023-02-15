class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    # Try Kadane's algorithm starting at every index
    # TLE, time complexity n^2

    c_idx = lambda x: x % len(nums)

    max_sum = float('-inf')
    
    for i in range(len(nums)):
      current_sum = 0
      for j in range(i, i+len(nums)):
        j = c_idx(j)
        current_sum = max(nums[j], current_sum+nums[j])
        max_sum = max(max_sum, current_sum)

    return max_sum

