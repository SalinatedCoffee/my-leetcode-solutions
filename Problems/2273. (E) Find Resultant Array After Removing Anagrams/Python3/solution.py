class Solution:
  def removeAnagrams(self, words: List[str]) -> List[str]:
    # dictionaries

    n = len(words)
    res = [words[0]]
    freq_top = Counter(words[0])

    for i in range(1, n):
      freq = Counter(words[i])
      if freq_top == freq:
        continue
      res.append(words[i])
      freq_top = freq

    return res

