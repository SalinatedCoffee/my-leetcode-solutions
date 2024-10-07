class Solution:
  def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    # longest common pre/suffix

    s1, s2 = sentence1.split(), sentence2.split()
    # ensure that len(s1) >= len(s2)
    if len(s1) < len(s2):
      s1, s2 = s2, s1
    m, n = len(s1), len(s2)

    # find longest common prefix
    i, j = 0, 0
    while i < m and j < n and s1[i] == s2[j]:
      i += 1
      j += 1
    if j == n:
      return True
    # find longest common suffix
    i, k = m-1, n-1
    while 0 <= i and 0 <= k and s1[i] == s2[k]:
      i -= 1
      k -= 1
    if k == -1:
      return True

    return j > k

