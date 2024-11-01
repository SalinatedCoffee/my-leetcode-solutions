class Solution:
  def makeFancyString(self, s: str) -> str:
    # sliding window

    n = len(s)
    # sanity check
    if n < 3:
      return s
    # avoid string contatenations
    res = [s[0], s[1]]
    for i in range(2, n):
      if not (s[i-2] == s[i-1] == s[i]):
        res.append(s[i])

    return ''.join(res)

