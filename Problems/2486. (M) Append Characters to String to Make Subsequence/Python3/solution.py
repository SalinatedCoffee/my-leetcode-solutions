class Solution:
  def appendCharacters(self, s: str, t: str) -> int:
    # greedy

    m, n = len(s), len(t)

    j = 0
    # match characters of t with their earliest counterpart in s
    for i in range(m):
      if j < n and s[i] == t[j]:
        j += 1

    return n - j

