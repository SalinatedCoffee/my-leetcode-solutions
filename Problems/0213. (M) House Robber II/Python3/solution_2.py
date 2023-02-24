class Solution:
  def rob(self, nums: List[int]) -> int:
    # dynamic programming, zip two traversals into one

    # sanity check
    if len(nums) == 1:
      return nums[0]

    res = -1
    for start in range(2):
      prev_2 = 0
      prev = nums[start]
      for i in range(start+1, len(nums)-1+start):
        temp = prev
        prev = max(prev_2+nums[i], prev)
        prev_2 = temp
      res = max(res, prev)
    
    return res

