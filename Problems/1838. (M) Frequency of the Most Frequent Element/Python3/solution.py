class Solution:
  def maxFrequency(self, nums: List[int], k: int) -> int:
    # sliding window on sorted list

    n = len(nums)
    nums.sort()

    ret = -1
    l, cost = 0, 0
    for i in range(1, n):
      # compute cost of new window
      cost += (i - l) * (nums[i] - nums[i-1])
      # contract window until cost is acceptable
      while cost > k and l <= i:
        cost -= (nums[i] - nums[l])
        l += 1
      # update largest window size accordlingly
      ret = max(ret, i - l + 1)
    
    return ret if ret != -1 else 1

