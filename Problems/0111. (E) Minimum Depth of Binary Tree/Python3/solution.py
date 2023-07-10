class Solution:
  def minDepth(self, root: Optional[TreeNode]) -> int:
    # iterative BFS

    nodes = deque()
    nodes.append((root, 1))
    while nodes:
      cur, d = nodes.popleft()
      if not cur:
        continue
      if not cur.left and not cur.right:
        return d
      nodes.append((cur.left, d+1))
      nodes.append((cur.right, d+1))
    
    return 0

