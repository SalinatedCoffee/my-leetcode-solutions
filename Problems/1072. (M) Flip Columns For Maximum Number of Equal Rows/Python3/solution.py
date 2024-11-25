class Solution:
  def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    # brute force

    m, n = len(matrix), len(matrix[0])
    res = 0
    for row in matrix:
      # compute compliment of current row
      row_comp = [1 ^ x for x in row]
      count = 0
      # count rows in matrix equal to current or compliment of current row
      for other_row in matrix:
        count += 1 if row == other_row or row_comp == other_row else 0
      res = max(res, count)

    return res

