class Solution:
  def minimumReplacement(self, nums: List[int]) -> int:
    # greedy

    n = len(nums)
    ret = 0
    for i in range(n-2, -1, -1):
      # adjacent pair already sorted
      if nums[i] <= nums[i+1]:
        continue
      # determine divisibility of nums[i] by nums[i+1]
      if nums[i] % nums[i+1] == 0:
        pieces = nums[i] // nums[i+1]
      else:
        pieces = nums[i] // nums[i+1] + 1
      ret += pieces - 1
      nums[i] = nums[i] // pieces
    
    return ret

