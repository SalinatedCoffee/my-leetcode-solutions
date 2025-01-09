class Solution:
  def prefixCount(self, words: List[str], pref: str) -> int:
    # brute force

    m = len(pref)
    res = 0
    for word in words:
      if m <= len(word) and word[:m] == pref:
        res += 1

    return res

