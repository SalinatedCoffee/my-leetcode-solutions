class Solution:
  def minSteps(self, n: int) -> int:
    # recursion
    
    self.ret, self.steps = float('inf'), 0

    def recurse(s, c):
      if s == n:
        self.ret = min(self.ret, self.steps)
        return
      if s + c > n:
        return
      self.steps += 1
      # paste
      if c > 0:
        recurse(s+c, c)
      # copy
      if s != c:
        recurse(s, s)
      self.steps -= 1
    
    recurse(1, 0)

    return self.ret

