class Solution:
  def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
    # greedy

    m, n = len(rowSum), len(colSum)
    # current sums of rows and columns
    c_rowSum, c_colSum = [0] * m, [0] * n
    ret = [[0]*n for _ in range(m)]
    for i in range(m):
      for j in range(n):
        # greedily assign valid value to current element of matrix
        ret[i][j] = min(rowSum[i] - c_rowSum[i], colSum[j] - c_colSum[j])
        c_rowSum[i] += ret[i][j]
        c_colSum[j] += ret[i][j]

    return ret

