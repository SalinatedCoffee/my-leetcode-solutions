class Solution:
  def generateMatrix(self, n: int) -> List[List[int]]:
    # process edges and shrink
    
    ret = [[n**2]*n for _ in range(n)]
    l, h = 0, n-1
    c = 1
    while l < h:
      for i in range(l, h):
        ret[l][i] = c
        c += 1
      for i in range(l, h):
        ret[i][h] = c
        c += 1
      for i in range(h, l-1, -1):
        ret[h][i] = c
        c += 1
      for i in range(h-1, l, -1):
        ret[i][l] = c
        c += 1
      l += 1
      h -= 1
    
    return ret

