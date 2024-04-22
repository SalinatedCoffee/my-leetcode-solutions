class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    # iterative BFS

    nodes = deque([("0000", 0)])
    visited = set()
    while nodes:
      cur, d = nodes.popleft()
      if cur in visited:
        continue
      if cur == target:
        return d
      visited.add(cur)
      for i in range(len(target)):
        digit = int(cur[i]) + 10
        l, h = (digit - 1) % 10, (digit + 1) % 10
        nodes.append((cur[:i] + str(l) + cur[i+1:], d+1))
        nodes.append((cur[:i] + str(h) + cur[i+1:], d+1))


    return -1

