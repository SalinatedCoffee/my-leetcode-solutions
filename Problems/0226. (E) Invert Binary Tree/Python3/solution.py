class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # recursively swap subtrees
    
    if root is not None:
      left = self.invertTree(root.right)
      right = self.invertTree(root.left)
      root.left, root.right = left, right
    return root

