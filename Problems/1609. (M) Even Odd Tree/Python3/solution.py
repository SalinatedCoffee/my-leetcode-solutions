class Solution:
  def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
    # iterative BFS

    nodes = deque([(root, 0)])
    height, prev = 0, 0
    while nodes:
      node, h = nodes.popleft()
      if node.left:
        nodes.append((node.left, h+1))
      if node.right:
        nodes.append((node.right, h+1))
      # check evenness
      if h % 2 == node.val % 2:
        return False
      # check for height change
      if height != h:
        height, prev = h, node.val
        continue
      # check for monotonicity
      if h % 2 and prev <= node.val:
          return False
      elif h % 2 == 0 and prev >= node.val:
          return False
      prev = node.val

    return True

