class Solution:
  def getLucky(self, s: str, k: int) -> int:

    # convert string of letters to string of integers
    res = int(''.join([str(ord(c) - ord('a') + 1) for c in s]))
    
    # perform conversions
    for _ in range(k):
      if res < 10:
        break
      t = 0
      while res:
        t += res % 10
        res //= 10
      res = t

    return res

