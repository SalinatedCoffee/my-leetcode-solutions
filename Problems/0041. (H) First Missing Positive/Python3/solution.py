class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    # modify array to mark existing values
    
    n = len(nums)
    # preprocess out of bounds values
    one = False
    for i in range(1, n+1):
      if nums[i-1] == 1:
        one = True
      elif nums[i-1] <= 0 or nums[i-1] > n:
        nums[i-1] = 1
    
    # 1 is special, so explicitly check its existence
    if not one:
      return 1

    # mark existing values
    for i in range(n):
      nums[abs(nums[i])-1] *= -1 if nums[abs(nums[i])-1] > 0 else 1
    
    # find first missing positive value
    for i in range(n):
      if nums[i] > 0:
        return i+1

    return n+1

