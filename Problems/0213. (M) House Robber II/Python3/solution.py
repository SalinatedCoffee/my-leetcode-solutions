class Solution:
  def rob(self, nums: List[int]) -> int:
    # dynamic programming, iterate two times

    # sanity check
    if len(nums) == 1:
      return nums[0]

    # dp variables for range [0,n-2]
    odd_prev_2 = 0
    odd_prev = nums[0]
    # dp variables for range [1,n-1]
    even_prev_2 = 0
    even_prev = nums[1]

    # iterate for range [0, n-2]
    for i in range(1, len(nums)-1):
      temp = odd_prev
      odd_prev = max(odd_prev_2+nums[i], odd_prev)
      odd_prev_2 = temp
    
    # iterate for range [1, n-1]
    for i in range(2, len(nums)):
      temp = even_prev
      even_prev = max(even_prev_2+nums[i], even_prev)
      even_prev_2 = temp
    
    # return larger value
    return max(odd_prev, even_prev)

