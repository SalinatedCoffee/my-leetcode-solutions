class Solution:
  def findComplement(self, num: int) -> int:
    # bit manipulation

    temp = num
    bits = 0
    while temp:
      bits += 1
      temp >>= 1

    return num ^ (2**bits - 1)

