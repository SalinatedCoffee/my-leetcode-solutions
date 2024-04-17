class Solution:
  def sumOfLeftLeaves(self, root: Optional[TreeNode], left: bool = False) -> int:
    # recursive DFS
  
    if root.left is None and root.right is None:
      return root.val if left else 0

    ret = self.sumOfLeftLeaves(root.left, True) if root.left else 0

    return ret + (self.sumOfLeftLeaves(root.right) if root.right else 0)

