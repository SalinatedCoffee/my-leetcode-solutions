class Solution:
  def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
    # brute force

    m, n = len(matrix), len(matrix[0])
    row_min = [float('inf')] * m
    for i in range(m):
      row_min[i] = min(matrix[i])
    
    for j in range(n):
      max_idx = 0
      col_max = 0
      for i in range(m):
        if col_max < matrix[i][j]:
          col_max = matrix[i][j]
          max_idx = i
      if col_max == row_min[max_idx]:
        return [col_max]

    return []

