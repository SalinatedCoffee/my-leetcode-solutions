class Solution:
  # top-down dynamic programming (memoization)

  def canCross(self, stones: List[int]) -> bool:
    self.n = len(stones)
    self.stones = stones
    # senots[i] is list index (stones) of stone at unit position i
    self.senots = {s:i for i, s in enumerate(stones)}

    return self.recurse(0, 0)
  
  @cache
  def recurse(self, i, j):
    # return whether end can be reached from stones[i] having jumped j previously
    if i == self.n - 1:
      return True
    nxt = [j-1, j, j+1]

    ret = False
    for n in nxt:
      if n > 0:
        if self.stones[i] + n in self.senots:
          ret |= self.recurse(self.senots[self.stones[i] + n], n)

    return ret

