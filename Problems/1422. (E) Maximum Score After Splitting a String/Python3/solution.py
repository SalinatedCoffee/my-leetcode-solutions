class Solution:
  def maxScore(self, s: str) -> int:
    # pre/suffix sums

    n = len(s)
    # zeros[i] is number of 0s to the left of s[i] inclusive
    zeros = [0] * n
    zeros[0] = 1 if s[0] == '0' else 0
    for i in range(1, n):
      if s[i] == '0':
        zeros[i] += 1
      zeros[i] += zeros[i-1]
      
    ones = 0
    ret = -1
    for i in range(n-1, 0, -1):
      if s[i] == '1':
        ones += 1
      ret = max(ret, ones + zeros[i-1])

    return ret

