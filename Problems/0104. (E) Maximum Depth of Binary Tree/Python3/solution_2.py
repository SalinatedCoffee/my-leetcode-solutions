class Solution:
  def maxDepth(self, root: TreeNode) -> int:
    # recursive solution
    
    # sanity check
    if root is None:
      return 0
    
    # recurse on children
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    
    # pick larger subtree
    if left > right:
      return left + 1
    else:
      return right + 1

