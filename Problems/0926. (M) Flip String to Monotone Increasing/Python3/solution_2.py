class Solution:
  def minFlipsMonoIncr(self, s: str) -> int:
    # if a string is monotonically increasing
    # its prefixes are also monotonically increasing, by induction
    # compute minimum flip count at current based on previous values
    # dynamic programming

   # number of 1s in prefix
    ones = 0
    # min. number of flips at i
    flips = 0

    for i in range(len(s)):
      if s[i] == '0':
        flips = min(ones, flips+1)
      else:
        ones += 1
    
    return flips

