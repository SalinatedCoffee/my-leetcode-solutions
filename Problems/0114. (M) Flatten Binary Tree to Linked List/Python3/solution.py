class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    # iterative DFS

    preorder = []

    nodes = [root]
    while nodes:
      cur = nodes.pop()
      if cur is None:
        continue
      preorder.append(cur)
      # push right child onto stack first for left-to-right traversal
      nodes.append(cur.right)
      nodes.append(cur.left)
    
    prev = root
    for node in preorder[1:]:
      prev.left = None
      prev.right = node
      prev = node

