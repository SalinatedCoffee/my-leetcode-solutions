class Solution:
  def minFlips(self, s: str) -> int:
    # brute force

    n = len(s)
    res = float('inf')
    # try all possible Type-1 operation configurations
    for i in range(n):
      # count number of flips required to make s alternating
      # where resulting string starts with either a 0 or a 1
      a, b = 0, 0
      ta, tb = 0, 1
      for j in range(i, n+i):
        c = s[j%n]
        a += 1 if int(c) == ta else 0
        b += 1 if int(c) == tb else 0
        ta ^= 1
        tb ^= 1
      res = min(res, min(a, b))


    return res

