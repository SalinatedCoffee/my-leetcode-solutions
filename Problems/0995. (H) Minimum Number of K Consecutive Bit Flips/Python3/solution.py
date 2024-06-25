class Solution:
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    # sliding window with auxillary array

    n = len(nums)
    # flipped[i] is whether i-th bit has been previously flipped
    flipped = [False] * n
    ret = 0
    # number of relevant previous windows flipped
    flips_prev = 0
    for i in range(n):
      # for window about to become irrelevant
      if i >= k:
        # if it was flipped, decrement relevant flip count
        if flipped[i - k]:
          flips_prev -= 1
      # if current bit needs to be flipped
      if flips_prev % 2 == nums[i]:
        # bit cannot be flipped, return -1
        if i + k > n:
          return -1
        flips_prev += 1
        flipped[i] = True
        ret += 1
    
    return ret

