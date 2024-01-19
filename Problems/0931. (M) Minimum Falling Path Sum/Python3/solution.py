class Solution:
  def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)

    n = len(matrix)

    @cache
    def recurse(i, j):
      # return minimum sum of falling path starting at matrix[i][j]
      if j < 0 or j >= n:
        return float('inf')
      if i == n - 1:
        return matrix[i][j]

      return matrix[i][j] + min(recurse(i+1, j), recurse(i+1, j-1), recurse(i+1, j+1))

    return min([recurse(0, i) for i in range(n)])

