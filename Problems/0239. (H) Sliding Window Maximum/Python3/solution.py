class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # sliding window with max heap

    n = len(nums)
    window = [(-1*nums[i], i) for i in range(k)]
    heapify(window)
    ret = [-1*window[0][0]]
    # index of start of window - 1
    idx = 0
    while idx < n-k:
      if nums[idx] == -1*window[0][0]:
        c = window[0][1]
        while c <= idx and window:
          heappop(window)
          if not window:
            break
          c = window[0][1]
      heappush(window, (-1*nums[idx+k], idx+k))
      ret.append(-1*window[0][0])
      idx += 1

    return ret

