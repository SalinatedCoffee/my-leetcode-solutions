class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # binary search

    m, n = len(matrix), len(matrix[0])
    
    l, h = 0, m*n-1
    while l <= h:
      i = (l + h) // 2
      i_v = matrix[i//n][i%n]
      if i_v == target:
        return True
      elif i_v > target:
        h = i - 1
      else:
        l = i + 1

    return False

