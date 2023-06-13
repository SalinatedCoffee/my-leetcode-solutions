class Solution:
  def equalPairs(self, grid: List[List[int]]) -> int:
    # dictionaries

    # key: string representation of row/col, value: frequency
    row = Counter()
    col = Counter()
    m, n = len(grid), len(grid[0])
    for i in range(m):
      c_str = ".".join(map(str,grid[i]))
      row[c_str] += 1
    for i in range(n):
      c_str = ".".join(map(str,[grid[n][i] for n in range(m)]))
      col[c_str] += 1
    
    ret = 0
    for key in row.keys():
      if key in col:
        ret += row[key] * col[key]
    
    return ret

