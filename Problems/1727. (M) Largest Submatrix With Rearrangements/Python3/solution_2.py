class Solution:
  def largestSubmatrix(self, matrix: List[List[int]]) -> int:
    # greedy algorithm without sorting

    m, n = len(matrix), len(matrix[0])
    prev_h = []
    ret = 0
    for i in range(m):
      h = []
      seen = [False] * n
      # extend runs from previous row if applicable
      for p_h, c in prev_h:
        if matrix[i][c] == 1:
          h.append((p_h+1, c))
          seen[c] = True
      # start new runs from this row if applicable
      for j in range(n):
        if not seen[j] and matrix[i][j] == 1:
          h.append((1, j))
      # compute submatrix sizes
      if h:
        ret = max(ret, *[l*(k+1)for k, (l, _) in enumerate(h)])
      prev_h = h
    
    return ret

