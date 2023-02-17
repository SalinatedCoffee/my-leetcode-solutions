class Solution:
  def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
    # inorder (LNR) to retrieve nodes in sorted order
    # compute min. diff during traversal

    self.prev = -1
    self.min_diff = 10**5+1
    def recurse(node):
      if node.left:
        recurse(node.left)
      if self.prev != -1:
        self.min_diff = min(self.min_diff, abs(self.prev-node.val))
      self.prev = node.val
      if node.right:
        recurse(node.right)
      
    recurse(root)

    return self.min_diff

