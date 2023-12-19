class Solution:
  def countSubstrings(self, s: str) -> int:
    # brute force

    n = len(s)
    self.ret = 0

    def count(i, j):
      while i >= 0 and j < n and s[i] == s[j]:
        self.ret += 1
        i -= 1
        j += 1
    
    for i in range(n):
      count(i, i)
      count(i, i+1)
    
    return self.ret

