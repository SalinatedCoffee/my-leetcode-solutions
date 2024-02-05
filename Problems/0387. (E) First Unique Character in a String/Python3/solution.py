class Solution:
  def firstUniqChar(self, s: str) -> int:
    # dictionary

    n = len(s)
    seen = {}
    for i in range(n):
      if s[i] in seen:
        seen[s[i]] = n
      else:
        seen[s[i]] = i

    return min(seen.values()) if min(seen.values()) != n else -1

