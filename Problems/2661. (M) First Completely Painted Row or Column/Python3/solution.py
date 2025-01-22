class Solution:
  def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
    # dictionaries

    m, n = len(mat), len(mat[0])
    # map value to coordinates in mat
    v2c = {}
    for i in range(m):
      for j in range(n):
        v2c[mat[i][j]] = (i, j)
    
    # sequentially paint values
    row, col = defaultdict(int), defaultdict(int)
    for i, v in enumerate(arr):
      r, c = v2c[v]
      row[r] += 1
      col[c] += 1
      if row[r] == n or col[c] == m:
        return i

    return -1

