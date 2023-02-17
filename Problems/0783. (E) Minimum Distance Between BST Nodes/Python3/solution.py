class Solution:
  def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    # inorder (LNR) to retrieve nodes in sorted order
    # generate inorder list of nodes and iterate across it

    self.vals = []
    def recurse(node):
      if node.left:
        recurse(node.left)
      self.vals.append(node.val)
      if node.right:
        recurse(node.right)
      
    recurse(root)
    min_diff = 10**5+1
    for i in range(1, len(self.vals)):
      diff = abs(self.vals[i] -self.vals[i-1])
      min_diff = min(min_diff, diff)
    
    return min_diff

