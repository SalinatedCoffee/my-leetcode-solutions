class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    # bit manipulation
    
    ret = 0
    # compute XOR sum of nums
    source = reduce(lambda x, y: x^y, nums)
    while source or k:
      if source & 1 != k & 1:
        ret += 1
      source >>= 1
      k >>= 1

    return ret

