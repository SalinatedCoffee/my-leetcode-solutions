class Solution:
  def customSortString(self, order: str, s: str) -> str:
    # brute force using dictionaries

    s_freq = Counter(s)
    ret = ""
    for c in order:
      if c in s_freq:
        ret += c * s_freq[c]
        del s_freq[c]
    
    for k, v in s_freq.items():
      ret += k * v

    return ret

