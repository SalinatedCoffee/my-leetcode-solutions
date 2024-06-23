class Solution:
  def longestSubarray(self, nums: List[int], limit: int) -> int:
    # sliding window with two heaps

    n = len(nums)
    l = 0
    min_h, max_h = [], []
    ret = 0
    for i in range(n):
      # add current item to heaps
      heappush(min_h, (nums[i], i))
      heappush(max_h, (-nums[i], i))
      # if window is valid, update longest length
      if -max_h[0][0] - min_h[0][0] <= limit:
        ret = max(ret, i - l + 1)
      # shrink window if it is invalid
      while -max_h[0][0] - min_h[0][0] > limit:
        # directly jump to offending element instead of incremental shrinks
        l = min(max_h[0][1], min_h[0][1]) + 1
        # remove invalidated elements from heaps
        while max_h and max_h[0][1] < l:
          heappop(max_h)
        while min_h and min_h[0][1] < l:
          heappop(min_h)

    return ret

