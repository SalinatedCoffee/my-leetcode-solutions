class Solution:
  def closeStrings(self, word1: str, word2: str) -> bool:
    # dictionaries

    # check for matching 'histograms'
    freq = Counter(Counter(word1).values())
    for v in Counter(word2).values():
      if freq[v] == 0:
        return False
      freq[v] -= 1

    # check if both strings have same set of unique letters
    return set(word1) == set(word2)

