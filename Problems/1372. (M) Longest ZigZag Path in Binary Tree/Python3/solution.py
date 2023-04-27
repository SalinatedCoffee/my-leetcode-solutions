class Solution:
  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    # recursive DFS
    pathLength = 0

    def dfs(node, goLeft, steps):
      if not node:
        return
      nonlocal pathLength
      pathLength = max(pathLength, steps)
      # node was right child
      if goLeft:
        dfs(node.left, False, steps+1)
        dfs(node.right, True, 1)
      # node was left child
      else:
        dfs(node.left, False, 1)
        dfs(node.right, True, steps+1)
    
    # root has no parent, so direction does not matter
    dfs(root, False, 0)
    # dfs(root, True, 0) would also work

    return pathLength

