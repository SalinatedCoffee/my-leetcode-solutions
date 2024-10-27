class Solution:
  def countSquares(self, matrix: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)

    m, n = len(matrix), len(matrix[0])

    # return number of square submatrices containing only 1s
    # where the upper left corner of the largest submatrix is matrix[i][j]
    @cache
    def recurse(i, j):
      if i == m or j == n or matrix[i][j] == 0:
        return 0
      r, d, b = recurse(i, j+1), recurse(i+1, j+1), recurse(i+1, j)
      
      return 1 + min(r, d, b)
    
    res = 0
    for i in range(m):
      for j in range(n):
        res += recurse(i, j)

    return res

