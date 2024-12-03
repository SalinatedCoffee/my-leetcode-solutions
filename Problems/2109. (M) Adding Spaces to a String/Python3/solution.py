class Solution:
  def addSpaces(self, s: str, spaces: List[int]) -> str:
    # two pointers

    m, n = len(spaces), len(s)
    # construct string as list of characters for efficiency
    res = []
    idx = 0
    for i in range(n):
      if idx < m and i == spaces[idx]:
        res.append(' ')
        idx += 1
      res.append(s[i])

    return "".join(res)

