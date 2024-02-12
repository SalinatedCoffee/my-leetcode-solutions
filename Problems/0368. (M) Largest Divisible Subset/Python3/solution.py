class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    # dynamic programming on sorted list

    n = len(nums)
    nums.sort()
    # size[i] is largest size of subset ending with nums[i]
    # prev[i] is index if previous element of nums[i] within subset
    size, prev = [1]*n, [-1]*n
    m_idx = 0
    for i in range(n):
      for j in range(i):
        if nums[i] % nums[j] == 0:
          if size[i] < 1 + size[j]:
            size[i] = 1 + size[j]
            prev[i] = j
      if size[i] > size[m_idx]:
        m_idx = i

    ret = []
    while m_idx != -1:
      ret.insert(0, nums[m_idx])
      m_idx = prev[m_idx]

    return ret

