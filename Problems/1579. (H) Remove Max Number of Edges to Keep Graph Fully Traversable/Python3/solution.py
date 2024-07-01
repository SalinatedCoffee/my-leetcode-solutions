class Solution:
  class UnionFind:
    def __init__(self, size):
      self._components = size
      self._p = [i for i in range(size)]
    
    def ufind(self, a):
      while a != self._p[a]:
        a = self._p[a]
      return a
    
    def uunion(self, a, b):
      pa, pb = self.ufind(a), self.ufind(b)
      if pa == pb:
        return False
      # reversing inequality gives TLE? will need to examine this later
      if pa > pb:
        self._p[pb] = pa
      else:
        self._p[pa] = pb
      self._components -= 1
      return True
    
    def ucomponents(self):
      return self._components

  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    # union find

    alice, bob = self.UnionFind(n), self.UnionFind(n)
    # sort edges by type
    edges.sort(reverse=True)
    idx = 0
    edge_count = 0
    # for each edge, only add it if it would reduce the number of components
    while idx < len(edges):
      a, b = edges[idx][1]-1, edges[idx][2]-1
      match edges[idx][0]:
        # add type 3 edges first
        case 3:
          test = alice.uunion(a, b) and bob.uunion(a, b)
        # then the other 2 types
        case 2:
          test = bob.uunion(a, b)
        case 1:
          test = alice.uunion(a, b)
      if test:
        edge_count += 1
        # return early whenever graph is traversable by both
        if alice.ucomponents() == 1 and bob.ucomponents() == 1:
          return len(edges) - edge_count
      idx += 1
    
    return -1

