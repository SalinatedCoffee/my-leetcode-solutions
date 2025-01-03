class Solution:
  def waysToSplitArray(self, nums: List[int]) -> int:
    # prefix sums

    n = len(nums)
    pre = nums[:]
    for i in range(1, n):
      pre[i] += pre[i-1]
    
    res = 0
    for i in range(n-1):
      if pre[i] >= pre[-1] - pre[i]:
        res += 1

    return res

