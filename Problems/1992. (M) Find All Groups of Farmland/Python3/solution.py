class Solution:
  def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
    # iterative DFS

    m, n = len(land), len(land[0])
    vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    ret = []
    visited = set()
    for r in range(m):
      for c in range(n):
        # if current cell is land and not yet traversed, run DFS
        if land[r][c] and (r, c) not in visited:
          nodes = [(r, c)]
          max_y, max_x = 0, 0
          while nodes:
            c_i, c_j = nodes.pop()
            if (c_i, c_j) in visited:
              continue
            visited.add((c_i, c_j))
            max_y = max(max_y, c_i)
            max_x = max(max_x, c_j)
            for dy, dx in vec:
              ny, nx = c_i + dy, c_j + dx
              if 0 <= ny < m and 0 <= nx < n and land[ny][nx]:
                nodes.append((ny, nx))
          # (r, c) is guaranteed to be upper-left square of farmland
          ret.append([r, c, max_y, max_x])

    return ret

