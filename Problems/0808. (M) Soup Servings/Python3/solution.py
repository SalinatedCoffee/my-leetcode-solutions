class Solution:
  # top-down dynamic programming (memoization)

  def soupServings(self, n: int) -> float:
    self.vectors = [(-100,0), (-75,-25), (-50,-50), (-25,-75)]
    if n >= 4800:
      return 1

    return self.recurse(n, n)
  
  @cache
  def recurse(self, a, b):
    # returns desired probability when a and b ml of soup remains

    if a <= 0 and b <= 0:
      return 0.5
    if a <= 0:
      return 1
    if b <= 0:
      return 0

    tot = 0
    for da, db in self.vectors:
      tot += self.recurse(a+da, b+db)

    return tot * 0.25

