class Solution:
  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # sliding window with deque

    n = len(nums)
    window = deque(nums[:k])
    ret = []
    idx = k
    while idx < n:
      ret.append(max(window))
      window.popleft()
      window.append(nums[idx])
      idx += 1
    ret.append(max(window))

    return ret

