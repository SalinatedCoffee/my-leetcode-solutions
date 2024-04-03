class Solution:
  def recoverTree(self, root: Optional[TreeNode]) -> None:
    # recursion
    
    self.prev = None
    err = []

    # perform inorder traversal, save references to nodes that are out of order
    def recurse(node):
      if node.left:
        recurse(node.left)
      if self.prev and self.prev.val > node.val:
        err.extend([self.prev, node])
      self.prev = node
      if node.right:
        recurse(node.right)
    
    recurse(root)
    # swap values back into their correct nodes
    err[0].val, err[-1].val = err[-1].val, err[0].val

