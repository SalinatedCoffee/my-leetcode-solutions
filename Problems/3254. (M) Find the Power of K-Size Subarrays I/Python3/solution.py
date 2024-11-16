class Solution:
  def resultsArray(self, nums: List[int], k: int) -> List[int]:
    # sliding window
    
    # handle edge case
    if k == 1:
      return nums

    n = len(nums)
    # intialize window
    c = 0
    for i in range(1, k-1):
      if nums[i-1] < nums[i] and nums[i] - nums[i-1] == 1:
        c += 1
    # slide window over nums
    res = []
    for i in range(k-1, n):
      if nums[i-1] < nums[i] and nums[i] - nums[i-1] == 1:
        c += 1
      if c == k-1:
        res.append(nums[i])
      else:
        res.append(-1)
      if nums[i-k+1] < nums[i-k+2] and nums[i-k+2] - nums[i-k+1] == 1:
        c -= 1

    return res

