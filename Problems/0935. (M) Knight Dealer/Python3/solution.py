class Solution:
  # top-down dynamic programming (memoization)

  def knightDialer(self, n: int) -> int:
    v = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
    mod = 10**9 + 7

    @cache
    def recurse(pos, t):
      # return number of dialable numbers of length t starting at pos
      if t == 1:
        return 1
      y, x = pos
      ret = 0
      for dy, dx in v:
        ny, nx = y+dy, x+dx
        if (0 <= ny <= 2 and 0 <= nx <= 2) or (ny == 3 and nx == 1):
          ret += recurse((ny, nx), t-1)
      
      return ret % mod

    ret = 0
    for i in range(3):
      for j in range(3):
        ret += recurse((i, j), n)
    ret += recurse((3, 1), n)

    return ret % mod

  
  

