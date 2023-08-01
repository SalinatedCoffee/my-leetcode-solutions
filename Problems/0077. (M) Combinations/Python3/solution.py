class Solution:
  # backtracking
  
  def combine(self, n: int, k: int) -> List[List[int]]:
    self.ret = []
    for i in range(1, n+1):
      self.recurse([], i, n, k)
    return self.ret
  
  def recurse(self, l, s, n, k):
    l.append(s)
    if len(l) == k:
      self.ret.append(copy.copy(l))
      l.pop()
      return
    if s > n:
      return
    for i in range(s, n):
      self.recurse(l, i+1, n, k)
    l.pop()

