class Solution:
  def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
    # bit manipulation

    n = len(nums)
    mask = (1 << maximumBit) - 1
    res = [0] * n
    cur = 0
    for i in range(n):
      cur ^= nums[i]
      res[n-1-i] = cur ^ mask

    return res

