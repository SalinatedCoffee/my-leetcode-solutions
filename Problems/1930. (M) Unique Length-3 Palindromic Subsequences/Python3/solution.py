class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    # manual counting using sets
    
    n = len(s)
    chars = set(s)
    ret = 0

    # for each unique character in s...
    for c in chars:
      # ...find 'widest' pair, if it exists
      l, r = 0, 0
      for i in range(n):
        if s[i] == c:
          l = i + 1
          break
      for i in range(n - 1, -1, -1):
        if s[i] == c:
          r = i
          break
      center = set()
      # count unique characters flanked by pair
      for i in range(l, r):
        center.add(s[i])
      ret += len(center)

    return ret

