class Solution:
  def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    # iterative BFS

    # sanity check
    if grid[0][0]:
      return -1

    n = len(grid)
    nodes = deque()
    visited = set()
    nodes.append((0,0,1))
    visited.add((0,0))
    while nodes:
      c_y, c_x, d = nodes.popleft()
      if c_y == n-1 and c_x == n-1:
        return d
      nxt = [(c_y+1,c_x), (c_y,c_x+1), (c_y-1,c_x), (c_y,c_x-1),
        (c_y+1,c_x-1), (c_y+1,c_x+1), (c_y-1,c_x-1), (c_y-1,c_x+1)]
      for n_c in nxt:
        if n_c not in visited and 0 <= n_c[0] < n and 0 <= n_c[1] < n and not grid[n_c[0]][n_c[1]]:
          visited.add((n_c[0],n_c[1]))
          nodes.append((n_c[0],n_c[1],d+1))

    return -1

