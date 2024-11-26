class Solution:
  def maxMatrixSum(self, matrix: List[List[int]]) -> int:
    # greedy algorithm

    m, n = len(matrix), len(matrix[0])
    # minimum absolute value of element in matrix
    abs_min = float('inf')
    # number of negative values in matrix
    neg_vals = 0
    # sum of absolute value of each element in matrix
    mat_tot = 0
    for i in range(m):
      for j in range(n):
        if matrix[i][j] < 0:
          neg_vals += 1
        mat_tot += abs(matrix[i][j])
        abs_min = min(abs_min, abs(matrix[i][j]))

    return mat_tot - (0 if neg_vals % 2 == 0 else 2*abs_min)

