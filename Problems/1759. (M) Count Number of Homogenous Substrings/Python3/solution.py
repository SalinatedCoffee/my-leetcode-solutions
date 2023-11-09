class Solution:
  def countHomogenous(self, s: str) -> int:
    # math

    n = len(s)
    if n == 1:
      return 1

    mod = 10**9 + 7
    ret = 0
    size = 1
    for i in range(1, n):
      if s[i] != s[i-1]:
        ret += size * (size + 1) // 2
        ret %= mod
        size = 0
      size += 1

    ret += size * (size + 1) // 2
    ret %= mod

    return ret

