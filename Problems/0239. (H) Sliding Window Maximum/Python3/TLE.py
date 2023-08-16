class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # sliding window

    n = len(nums)
    ret = []
    idx = k
    while idx < n:
      ret.append(max(nums[idx-k:idx))
      idx += 1
    ret.append(max(nums[idx-k:idx))

    return ret

