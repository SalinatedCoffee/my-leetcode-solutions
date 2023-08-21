class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    # brute force

    n = len(s)
    for i in range(1, n):
      if not n % i:
        b, c = False, 0
        while c < n:
          if s[:i] != s[c:c+i]:
            b = True
            break
          c += i
        if not b:
          return True
    
    return False

