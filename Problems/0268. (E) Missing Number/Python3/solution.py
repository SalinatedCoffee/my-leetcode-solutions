class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    # math
    
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)

