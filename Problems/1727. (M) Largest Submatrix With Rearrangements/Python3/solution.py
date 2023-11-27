class Solution:
  def largestSubmatrix(self, matrix: List[List[int]]) -> int:
    # greedy algorithm on sorted list

    m, n = len(matrix), len(matrix[0])
    # preprocess matrix
    runs = [[0]*n for _ in range(m)]
    for i in range(n):
      run = 0
      for j in range(m):
        if matrix[j][i] == 1:
          run += 1
        else:
          run = 0
        runs[j][i] = run

    # determine maximum submatrix size
    ret = -1
    for row in runs:
      row.sort(reverse=True)
      for i in range(n):
        ret = max(ret, (i+1)*row[i])
      
    return ret

