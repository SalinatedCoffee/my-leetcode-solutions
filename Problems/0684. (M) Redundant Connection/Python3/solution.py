class Solution:
  def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    # union-find

    n = len(edges)
    # value of p[i] is label of set containing i
    p = [i for i in range(n)]

    # utility function that returns label of set containing a
    def ufind(a):
      pa = p[a]
      while pa != a:
        a = pa
        pa = p[a]
      return a

    # utility function that merges sets with label pa and pb
    def uunion(pa, pb):
      if pa > pb:
        p[pa] = pb
      else:
        p[pb] = pa
    
    # process edges
    for u, v in edges:
      pu, pv = ufind(u-1), ufind(v-1)
      # cycle detected
      if pu == pv:
        return [u, v]
      uunion(pu, pv)

    # this line is never reached given problem constraints
    return [-1, -1]

