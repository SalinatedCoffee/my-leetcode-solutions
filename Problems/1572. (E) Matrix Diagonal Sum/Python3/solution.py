class Solution:
  def diagonalSum(self, mat: List[List[int]]) -> int:
    # iteration
    
    n = len(mat)
    ret = 0
    for r in range(n//2):
      ret += mat[r][r] + mat[r][n-1-r] + mat[n-1-r][r] + mat[n-1-r][n-1-r]
    if n % 2:
      ret += mat[n//2][n//2]

    return ret

