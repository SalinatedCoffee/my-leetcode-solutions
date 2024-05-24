class Solution:
  def distributeCoins(self, root: Optional[TreeNode]) -> int:
    # postorder(LRN) traversal

    self.ret = 0

    def recurse(node):
      # return number of coins required/left over from the tree rooted at node
      if node is None:
        return 0
      left = recurse(node.left)
      right = recurse(node.right)
      self.ret += abs(left) + abs(right)

      return node.val - 1 + left + right
    
    recurse(root)

    return self.ret

