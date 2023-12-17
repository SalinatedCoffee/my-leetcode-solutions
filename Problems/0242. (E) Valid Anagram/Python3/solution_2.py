class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # dictionaries

    freq_s, freq_t = defaultdict(int), defaultdict(int)
    chars = set()
    for c in s:
      freq_s[c] += 1
      chars.add(c)
    for c in t:
      freq_t[c] += 1
      chars.add(c)
    
    for c in chars:
      if freq_s[c] != freq_t[c]:
        return False
    
    return True

