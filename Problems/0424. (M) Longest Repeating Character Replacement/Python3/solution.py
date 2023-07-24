class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # brute-force sliding window
    
    n = len(s)
    ret = 0
    for c in string.ascii_uppercase:
      freq = 0
      l = 0
      for i in range(n):
        if s[i] != c:
          freq += 1
        while l < n and freq > k:
          if s[l] != c:
            freq -= 1
          l += 1
        ret = max(ret, i-l+1)
    
    return ret
    
