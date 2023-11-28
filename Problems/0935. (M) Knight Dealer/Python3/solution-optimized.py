class Solution:
  # top-down dynamic programming (memoization)

  def knightDialer(self, n: int) -> int:
    v = [[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
    mod = 10**9 + 7

    @cache
    def recurse(pos, t):
      # return number of dialable numbers of length t starting at pos
      if t == 1:
        return 1
      ret = 0
      for nxt in v[pos]:
        ret += recurse(nxt, t-1)
      
      return ret % mod

    ret = 0
    for i in range(10):
      ret += recurse(i, n)

    return ret % mod

