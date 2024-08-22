class Solution:
  def findComplement(self, num: int) -> int:
    # brute force bit manipulation

    bits = []
    while num:
      bits.append(num & 1)
      num >>= 1
    
    ret = 0
    for bit in reversed(bits):
      ret <<= 1
      ret |= bit ^ 1

    return ret

