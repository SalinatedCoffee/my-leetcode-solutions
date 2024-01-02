class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # two pointers on sorted lists

    m, n = len(g), len(s)
    g.sort()
    s.sort()
    i, j = 0, 0
    ret = 0
    while i < m and j < n:
      if g[i] <= s[j]:
        ret += 1
        i += 1
      j += 1

    return ret

