class Solution:
  def removeStones(self, stones: List[List[int]]) -> int:
    # union find

    n = len(stones)
    p = {(i, j):(i, j) for i, j in stones}
    self.components = n

    def ufind(a):
      pa = p[a]
      while pa != a:
        a = pa
        pa = p[a]
      return a

    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if pa != pb:
        self.components -= 1
        p[pa] = pb
    
    for i in range(n):
      a = stones[i]
      for j in range(i+1, n):
        b = stones[j]
        # merge nodes if they share a row or column
        if a[0] == b[0] or a[1] == b[1]:
          uunion(tuple(stones[(i)]), tuple(stones[j]))

    return n - self.components

