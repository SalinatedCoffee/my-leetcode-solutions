class Solution:
  def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    # simulation

    VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    res = [[-1] * n for _ in range(m)]
    y, x, v = 0, 0, 0
    cur = head
    while cur:
      res[y][x] = cur.val
      ny, nx = y + VEC[v][0], x + VEC[v][1]
      if ny < 0 or nx < 0 or ny >= m or nx >= n or res[ny][nx] != -1:
        v = (v + 1) % 4
      y, x = y + VEC[v][0], x + VEC[v][1]
      cur = cur.next

    return res

