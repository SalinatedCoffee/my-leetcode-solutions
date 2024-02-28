class Solution:
  def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
    # iterative BFS

    ret, max_d = 0, -1
    queue = deque([(root, 0)])
    while queue:
      node, d = queue.popleft()
      if d > max_d:
        ret, max_d = node.val, d
      if node.left:
        queue.append((node.left, d+1))
      if node.right:
        queue.append((node.right, d+1))

    return ret

