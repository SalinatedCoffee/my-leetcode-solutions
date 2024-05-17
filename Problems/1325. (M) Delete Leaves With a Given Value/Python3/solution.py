class Solution:
  def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    # recursion

    if root is None:
      return None

    root.left = self.removeLeafNodes(root.left, target)
    root.right = self.removeLeafNodes(root.right, target)
    
    if not root.left and not root.right:
      return None if root.val == target else root

    return root

