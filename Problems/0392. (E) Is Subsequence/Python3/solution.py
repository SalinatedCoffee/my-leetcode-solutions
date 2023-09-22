class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    # brute force

    # sanity check
    if len(s) == 0:
      return True

    n, m = len(t), len(s)
    i = 0
    for c in t:
      if c == s[i]:
        i += 1
      if i == m:
        return True

    return False

