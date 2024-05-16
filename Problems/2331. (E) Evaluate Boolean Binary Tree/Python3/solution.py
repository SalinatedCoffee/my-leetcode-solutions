class Solution:
  def evaluateTree(self, root: Optional[TreeNode]) -> bool:
    # recursively evaluate subtrees

    match root.val:
      case 0:
        return False
      case 1:
        return True
      case 2:
        return self.evaluateTree(root.left) or self.evaluateTree(root.right)
      case 3:
        return self.evaluateTree(root.left) and self.evaluateTree(root.right)

    # given problem constraints, this line will never be reached
    return False

