class Solution:
  def minFlips(self, mat: List[List[int]]) -> int:
    # recursive DFS
    
    m, n = len(mat), len(mat[0])
    # number of elements in matrix
    k = m * n
    VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # translate index to matrix coordinates
    ntoc = lambda x: (x//n, x%n)
    # number of times each element was flipped
    cnt = [[0]*n for _ in range(m)]
    def recurse(i, f):
      # return minimum number of flips required to make mat a zero matrix
      # starting at the i-th square(0-indexed) with f flips previously performed

      # base case
      if i == k:
        # return number of flips if mat is a zero matrix
        for j in range(k):
          r, c = ntoc(j)
          if cnt[r][c] % 2 != mat[r][c]:
            return float('inf')
        return f
      # get row and column number of i-th square
      r, c = ntoc(i)
      # flip squares and recurse
      cnt[r][c] += 1
      for dy, dx in VEC:
        ny, nx = r+dy, c+dx
        if 0 <= ny < m and 0 <= nx < n:
          cnt[ny][nx] += 1
      ret = recurse(i+1, f+1)
      # revert flip and recurse
      cnt[r][c] -= 1
      for dy, dx in VEC:
        ny, nx = r+dy, c+dx
        if 0 <= ny < m and 0 <= nx < n:
          cnt[ny][nx] -= 1

      return min(ret, recurse(i+1, f))

    ret = recurse(0, 0)

    return ret if ret != float('inf') else -1

