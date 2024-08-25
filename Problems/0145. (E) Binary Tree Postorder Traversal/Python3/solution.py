class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # recursive postorder traversal (LRN)

    self.ret = []
    def recurse(node):
      if not node:
        return
      recurse(node.left)
      recurse(node.right)
      self.ret.append(node.val)
    
    recurse(root)

    return self.ret

