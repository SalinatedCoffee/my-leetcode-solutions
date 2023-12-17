class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    # count

    atoi = lambda x: ord(x) - ord('a')
    freq_s = [0] * 26
    freq_t = [0] * 26
    for c in s:
      freq_s[atoi(c)] += 1
    for c in t:
      freq_t[atoi(c)] += 1
    
    for i in range(26):
      if freq_s[i] != freq_t[i]:
        return False
    
    return True

