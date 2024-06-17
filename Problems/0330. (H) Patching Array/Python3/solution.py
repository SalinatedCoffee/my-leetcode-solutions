class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    # greedy

    m = len(nums)
    ret = 0
    # current 'prefix sum'
    pre = 1
    idx = 0
    while pre <= n:
      # if no gap between current prefix array and current element
      if idx < m and nums[idx] <= pre:
        pre += nums[idx]
        idx += 1
      # otherwise, add new value to nums
      else:
        pre += pre
        ret += 1

    return ret

