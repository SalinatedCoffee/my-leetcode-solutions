class Solution:
  def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
    # iterative BFS

    if depth == 1:
      return TreeNode(val, root)
    
    nodes = deque([(root, 1)])
    while nodes:
      cur, d = nodes.popleft()
      if d == depth - 1:
        cur.left = TreeNode(val, cur.left)
        cur.right = TreeNode(val, None, cur.right)
      else:
        if cur.left:
          nodes.append((cur.left, d+1))
        if cur.right:
          nodes.append((cur.right, d+1))

    return root

