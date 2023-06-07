class Solution:
  def minFlips(self, a: int, b: int, c: int) -> int:
    # bit manipulation
    
    ret = 0
    while a or b or c:
      c_a = a & 1
      c_b = b & 1
      c_c = c & 1
      if c_c:
        ret += 1 if not (c_a | c_b) else 0
      else:
        ret += 1 if c_a else 0
        ret += 1 if c_b else 0
      a >>= 1
      b >>= 1
      c >>= 1
    
    return ret

