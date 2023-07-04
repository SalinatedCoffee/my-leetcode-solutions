class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    # bit manipulation  

    # count frequency of set bits
    bits = [0] * 32
    for n in nums:
      mask = 1
      for i in range(32):
        if n & mask:
          bits[i] += 1
        mask <<= 1
    
    # reconstruct singular integer
    ret = 0
    for i in range(31):
      if bits[i] % 3:
        ret |= 1 << i

    # set negative bit accordingly
    if bits[-1] % 3:
      ret -= (1 << 31)

    return ret

