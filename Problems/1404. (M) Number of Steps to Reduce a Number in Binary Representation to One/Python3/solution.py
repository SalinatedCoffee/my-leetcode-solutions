class Solution:
  def numSteps(self, s: str) -> int:
    # bit manipulation

    ret = 0
    # convert string to integer
    val = int(s, base=2)
    while val != 1:
      # perform appropriate operation and increment step count
      if val & 1:
        val += 1
      else:
        val >>= 1
      ret += 1

    return ret

