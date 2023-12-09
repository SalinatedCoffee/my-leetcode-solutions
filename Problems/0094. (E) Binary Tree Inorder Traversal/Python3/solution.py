class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive DFS (LNR traversal)

    ret = []

    def dfs(node):
      if node.left:
        dfs(node.left)
      ret.append(node.val)
      if node.right:
        dfs(node.right)
    
    if root:
      dfs(root)

    return ret

