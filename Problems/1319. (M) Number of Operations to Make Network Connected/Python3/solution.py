class Solution:
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    # union find

    # sanity check
    if len(connections) < n-1:
      return -1

    p = [i for i in range(n)]

    def ufind(a):
      pa = p[a]
      while pa != a:
        a = pa
        pa = p[a]
      return pa

    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if pa > pb:
        p[pb] = pa
      else:
        p[pa] = pb

    for u, v in connections:
      uunion(u, v)
    
    # count number of disconnected components
    components = set()
    for i in p:
      components.add(ufind(i))

    return len(components) - 1

