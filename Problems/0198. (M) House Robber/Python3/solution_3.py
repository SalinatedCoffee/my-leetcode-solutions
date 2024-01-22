class Solution:
  def rob(self, nums: List[int]) -> int:
    # space-optmized bottom-up dynamic programming (tabulation)

    # sanity check
    if not nums:
      return 0
    
    # maximum stolen up to 2nd previous house
    prev_2 = 0
    # maximum stolen up to previous house
    prev = nums[0]

    for i in range(1, len(nums)):
      # either steal from current or skip
      temp = prev
      prev = max(prev_2+nums[i], prev)
      prev_2 = temp
    
    return prev

