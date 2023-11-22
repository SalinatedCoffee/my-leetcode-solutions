class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    # BFS

    m = len(nums)
    nodes = deque([(0,0)])
    ret = []
    while nodes:
      r, c = nodes.popleft()
      ret.append(nums[r][c])
      if c == 0 and r + 1 < m:
        nodes.append((r + 1, c))
      if c + 1 < len(nums[r]):
        nodes.append((r, c + 1))

    return ret

