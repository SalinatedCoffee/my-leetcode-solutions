class Solution:
  def shortestPalindrome(self, s: str) -> str:
    # brute force

    n = len(s)
    s_rev = s[::-1]
    for i in range(n):
      if s[:n-i] == s_rev[i:]:
        return s_rev[:i] + s
  
    return ""

