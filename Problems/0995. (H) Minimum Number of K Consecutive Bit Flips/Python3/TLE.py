class Solution:
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    # sliding window with greedy algorithm

    n = len(nums)
    ret = 0
    for i in range(k-1, n):
      # if left-most bit of window is 1, don't do anything
      if nums[i - k + 1]:
        continue
      # otherwise, increment counter and perform k-bit flip
      ret += 1
      for j in range(i - k + 1, i + 1):
        nums[j] ^= 1

    # only return counter if all bits are raised
    return ret if sum(nums) == n else -1

