class Solution:
  def getSum(self, a: int, b: int) -> int:
    # bit manipulation

    # limit integers to 4 bytes
    mask = 0xFFFFFFFF
    
    # half adder logic
    while b:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    
    # two's complement, flip sign as necessary
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

