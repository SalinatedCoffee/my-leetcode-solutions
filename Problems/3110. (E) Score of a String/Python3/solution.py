class Solution:
  def scoreOfString(self, s: str) -> int:
    
    n = len(s)
    ret = 0
    for i in range(1, n):
      ret += abs(ord(s[i-1]) - ord(s[i]))

    return ret

