class Solution:
  def minOperations(self, nums: List[int], x: int) -> int:
    # sliding window

    n = len(nums)
    target = sum(nums) - x
    l, r = -1, 0
    m_len, cur = -1, 0
    while r < n:
      cur += nums[r]
      while l < r and cur > target:
        l += 1
        cur -= nums[l]
      # only update window size when window sum is exactly target
      if cur == target:
        m_len = max(m_len, r-l)
      r += 1
    
    return n - m_len if m_len != -1 else m_len

