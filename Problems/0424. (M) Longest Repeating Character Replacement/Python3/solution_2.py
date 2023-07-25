class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
    # optimized sliding window
    
    n = len(s)
    freq = Counter()
    max_freq = 0
    ret = 0
    l = 0
    for i in range(n):
      freq[s[i]] += 1
      max_freq = max(max_freq, freq[s[i]])
      if i - l + 1 - max_freq > k:
        freq[s[l]] -= 1
        l += 1
      ret = i - l + 1
    
    return ret
    
