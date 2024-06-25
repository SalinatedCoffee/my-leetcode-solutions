class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    # reverse postorder (RLN) with global variable

    # current sum of traversed node values
    self.sum = 0

    def recurse(node):
      if node.right:
        recurse(node.right)
      self.sum += node.val
      node.val = self.sum
      if node.left:
        recurse(node.left)
    
    recurse(root)

    # reuse provided tree
    return root

