class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    # iterative DFS

    # sanity check
    if not root:
      return 0
    
    depth = 0
    nodes = []
    nodes.append((root, 1))
    while nodes:
      cur, c_depth = nodes.pop()
      if not cur:
        continue
      # current node is leaf
      if not cur.left and not cur.right:
        depth = max(depth, c_depth)
      nodes.append((cur.left, c_depth+1))
      nodes.append((cur.right, c_depth+1))
    
    return depth

