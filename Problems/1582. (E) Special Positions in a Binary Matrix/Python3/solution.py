class Solution:
  def numSpecial(self, mat: List[List[int]]) -> int:
    # 2-pass
    
    m, n = len(mat), len(mat[0])
    row, col = [0]*m, [0]*n
    for i in range(m):
      for j in range(n):
        if mat[i][j]:
          row[i] += 1
          col[j] += 1
    
    ret = 0
    for i in range(m):
      for j in range(n):
        if mat[i][j] and row[i] == 1 and col[j] == 1:
          ret += 1

    return ret

