class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    # union find

    alice = self.UnionFind(n)
    bob = self.UnionFind(n)
    req_edges = 0
    idx = 0
    edges.sort(reverse=True)
    while idx < len(edges) and edges[idx][0] == 3:
      a_e = alice.uunion(edges[idx][1], edges[idx][2])
      b_e = bob.uunion(edges[idx][1], edges[idx][2])
      if a_e or b_e:
        req_edges += 1
      idx += 1
    while idx < len(edges) and edges[idx][0] == 2:
      if bob.uunion(edges[idx][1], edges[idx][2]):
        req_edges += 1
      idx += 1
    while idx < len(edges) and edges[idx][0] == 1:
      if alice.uunion(edges[idx][1], edges[idx][2]):
        req_edges += 1
      idx += 1
    if alice.components == 1 and bob.components == 1:
      return len(edges) - req_edges
    return -1
  
  class UnionFind:
    def __init__(self, n = 1):
      self._parents = [i for i in range(n+1)]
      self.components = n
      self._n = n

    def uunion(self, a, b):
      p_a, p_b = self._ufind(a), self._ufind(b)
      if not p_a or not p_b or p_a == p_b:
        return False
      if p_a > p_b:
        self._parents[p_b] = p_a
      else:
        self._parents[p_a] = p_b
      self.components -= 1
      return True
    
    def _ufind(self, a):
      if a > self._n:
        return None
      prev = a
      cur = self._parents[a]
      while cur != prev:
        prev = cur
        cur = self._parents[cur]
      return cur

