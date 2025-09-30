class NumMatrix:
  # prefix sums
  def __init__(self, matrix: List[List[int]]):
    m, n = len(matrix), len(matrix[0])
    # value of prefix[i][j] is the sum of values inside rectangle with
    # upper left corner (0, 0) and lower right corner (i, j)
    self._prefix = [[0] * n for _ in range(m)]
    self._prefix[0][0] = matrix[0][0]
    for j in range(1, n):
      self._prefix[0][j] = self._prefix[0][j-1] + matrix[0][j]
    for i in range(1, m):
      r_cur = 0
      for j in range(n):
        r_cur += matrix[i][j]
        self._prefix[i][j] = r_cur + self._prefix[i-1][j]


  def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    a = self._prefix[row2][col2]
    b = self._prefix[row1-1][col2] if row1 > 0 else 0
    c = self._prefix[row2][col1-1] if col1 > 0 else 0
    d = self._prefix[row1-1][col1-1] if (row1 > 0 and col1 > 0) else 0

    return a - b - c + d

