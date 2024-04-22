class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    # union find

    p = [i for i in range(n)]

    def ufind(a):
      while p[a] != a:
        a = p[a]

      return a
    
    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      p[pb] = pa
    
    for u, v in edges:
      uunion(u, v)
    
    return ufind(source) == ufind(destination)

