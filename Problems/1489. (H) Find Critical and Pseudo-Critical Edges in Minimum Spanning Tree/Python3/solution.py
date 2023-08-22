class Solution:
  # kruskal's algorithm

  class UFind:
    # union-find data structure
    # keeps track of size of largest set

    def __init__(self, n):
      # parent of element i
      self._p = [i for i in range(n)]
      # size of set i
      self._size = [1] * n
      # size of largest set
      self.largest = 1

    def find(self, a):
      pa = self._p[a]
      while pa != a:
        temp = pa
        a = pa
        pa = self._p[pa]
      return pa
    
    def union(self, a, b):
      # returns True if union is performed
      # False otherwise
      # rank by size

      pa, pb = self.find(a), self.find(b)
      if pa != pb:
        if self._size[pa] > self._size[pb]:
          self._p[pb] = pa
          self._size[pa] += self._size[pb]
          self.largest = max(self.largest, self._size[pa])
        else:
          self._p[pa] = pb
          self._size[pb] += self._size[pa]
          self.largest = max(self.largest, self._size[pb])
        return True
      return False


  def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    # preprocessing, use index as edge id and sort by weight in ascending order
    for i in range(len(edges)):
      edges[i].append(i)
    s_edges = sorted(edges, key=lambda x: x[2])

    # create MST of entire graph
    uf = self.UFind(n)
    mst_w = 0
    for u, v, w, _ in s_edges:
      if uf.union(u, v):
        mst_w += w
    
    ret = [[],[]]
    # for each and every edge
    for u, v, w, i in s_edges:
      # try creating MST ignoring that edge
      uf_c = self.UFind(n)
      mst_w_c = 0
      for a, b, w_c, j in s_edges:
        if i != j and uf_c.union(a, b):
          mst_w_c += w_c

      # check for criticality
      if uf_c.largest < n or mst_w_c > mst_w:
        ret[0].append(i)
        continue
      
      # try creating MST that includes that edge
      uf_c = self.UFind(n)
      mst_w_c = w
      uf_c.union(u, v)
      for a, b, w_c, j in s_edges:
        if i != j and uf_c.union(a, b):
          mst_w_c += w_c
      
      # check for pseudocriticality
      if mst_w_c == mst_w:
        ret[1].append(i)
    
    return ret

