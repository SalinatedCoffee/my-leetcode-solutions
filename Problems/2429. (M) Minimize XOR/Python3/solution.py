class Solution:
  def minimizeXor(self, num1: int, num2: int) -> int:
    # bit manipulation
    
    # count number of raised bits in num2
    bits = 0
    while num2:
      bits += 1 if num2 & 1 else 0
      num2 >>= 1
    
    # construct x
    res = 0
    temp = num1
    num1_len = 0
    while temp:
      temp >>= 1
      num1_len += 1
    mask = 1 << (num1_len - 1)
    while bits and mask:
      res |= num1 & mask
      bits -= 1 if num1 & mask else 0
      mask >>= 1
    mask = 1
    while bits:
      if num1 & mask == 0:
        res |= mask
        bits -= 1
      mask <<= 1

    return res

