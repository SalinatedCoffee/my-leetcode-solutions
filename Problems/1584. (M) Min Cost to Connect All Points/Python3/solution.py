class Solution:
  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # union-find based kruskal's algorithm

    n = len(points)
    # create list of all possible edges and sort by weight
    edges = []
    for i in range(n-1):
      for j in range(i+1, n):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        edges.append((i, j, abs(dx) + abs(dy)))
    edges.sort(key=lambda x: x[2])

    # find MST using kruskal's algorithm
    uf = UFind(n)
    ret = 0
    for u, v, w in edges:
      if uf.uunion(u, v):
        ret += w
      if uf.max_size == n:
        break
        
    return ret
      

class UFind:
  # implements basic union-find

  def __init__(self, cap):
    self._p = [i for i in range(cap)]
    self._s = [1] * cap
    self.max_size = 1
  
  def ufind(self, a):
    p_a = self._p[a]
    while p_a != a:
      a = p_a
      p_a = self._p[a]

    return p_a

  def uunion(self, a, b):
    p_a, p_b = self.ufind(a), self.ufind(b)

    if p_a == p_b:
      return False
    if self._s[p_a] <= self._s[p_b]:
      p_a, p_b = p_b, p_a
    self._p[p_b] = p_a
    self._s[p_a] += self._s[p_b]
    self.max_size = max(self.max_size, self._s[p_a])

    return True

