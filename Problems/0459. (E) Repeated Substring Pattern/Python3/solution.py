class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    # brute force

    n = len(s)
    for i in range(1, n):
      if not n % i:
        q = n // i
        if s[:i] * q == s:
          return True
    
    return False

