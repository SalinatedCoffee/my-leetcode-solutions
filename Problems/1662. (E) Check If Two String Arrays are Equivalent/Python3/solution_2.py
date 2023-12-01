class Solution:
  def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    # inline comparisons
    
    m, n = len(word1), len(word2)
    i, j = 0, 0
    a, b = 0, 0
    while i < m and j < n:
      while a < len(word1[i]) and b < len(word2[j]):
        if word1[i][a] != word2[j][b]:
          return False
        a += 1
        b += 1
      if a == len(word1[i]):
        a = 0
        i += 1
      if b == len(word2[j]):
        b = 0
        j += 1

    return True if a == 0 and b == 0 and i == m and j == n else False

