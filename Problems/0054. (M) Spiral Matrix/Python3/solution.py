class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    # walk edges and shrink

    ret = []
    m, n = len(matrix[0]), len(matrix)
    l, u = 0, 0
    r, d = m, n
    while l < r-1 and u < d-1:
      for i in range(l, r):
        ret.append(matrix[u][i])
      for i in range(u+1, d):
        ret.append(matrix[i][r-1])
      for i in range(r-2, l-1, -1):
        ret.append(matrix[d-1][i])
      for i in range(d-2, u, -1):
        ret.append(matrix[i][l])
      l += 1
      r -= 1
      u += 1
      d -= 1
    
    if len(ret) < m*n:
      if n > m:
        for i in range(u, d):
          ret.append(matrix[i][l])
      else:
        for i in range(l, r):
          ret.append(matrix[u][i])

    return ret

