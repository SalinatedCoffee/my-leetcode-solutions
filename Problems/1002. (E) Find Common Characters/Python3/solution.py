class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    # dictionaries

    n = len(words)
    # intersection of word character frequencies
    freq = Counter(words[0])
    for i in range(1, n):
      w_freq = Counter(words[i])
      for c in freq.keys():
        freq[c] = min(freq[c], w_freq[c])
    
    ret = []
    # build list of common characters
    for u, v in freq.items():
      ret.extend([u] * v)

    return ret

