class Solution:
  def shortestPathAllKeys(self, grid: List[str]) -> int:
    # iterative BFS with bit manipulation

    m = len(grid)
    n = len(grid[0])
    # more efficient to presearch keys and locks
    # instead of examining character of cell during traversal
    keys = set()
    locks = set()
    start = None
    for i in range(m):
      for j in range(n):
        if grid[i][j] in "abcdef":
          keys.add((i, j))
        elif grid[i][j] in "ABCDEF":
          locks.add((i, j))
        elif grid[i][j] == '@':
          start = (i, j)

    # bit representation of state where all keys have been collected
    all = 2**len(keys) - 1
    vectors = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = set()
    nodes = deque()
    nodes.append((start[0], start[1], 0, 0))
    visited.add((start[0], start[1], 0))
    while nodes:
      y, x, s, d = nodes.popleft()
      for dy, dx in vectors:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < m and 0 <= nx < n and grid[ny][nx] != '#':
          cell = grid[ny][nx]
          # new key picked up
          if (ny, nx) in keys and not ((1 << (ord(cell) - ord('a'))) & s):
            ns = (s | (1 << (ord(cell) - ord('a'))))
            # all keys have been collected
            if ns == all:
              return d + 1
            visited.add((ny, nx, ns))
            nodes.append((ny, nx, ns, d + 1))
          # unlockable lock
          elif (ny, nx) in locks and not (s & (1 << (ord(cell) - ord('A')))):
            continue
          elif (ny, nx, s) not in visited:
            visited.add((ny, nx, s))
            nodes.append((ny, nx, s, d + 1))
    
    return -1

