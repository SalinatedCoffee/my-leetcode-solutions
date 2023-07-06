class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # sliding window

    n = len(nums)
    l, tot = 0, 0
    ret = float('inf')
    for i in range(n):
      tot += nums[i]
      while tot >= target:
        ret = min(ret, i - l + 1)
        tot -= nums[l]
        l += 1

    return ret if ret != float('inf') else 0

