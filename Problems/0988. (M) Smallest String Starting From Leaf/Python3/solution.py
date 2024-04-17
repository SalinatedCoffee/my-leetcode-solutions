class Solution:
  def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
    # recursive DFS with string comparisons
    
    self.ret = None
    self.stack = []
    self.itoc = lambda x: chr(ord('a') + x)
    def recurse(node):
      self.stack.append(self.itoc(node.val))
      # if current node is leaf
      if node.left is None and node.right is None:
        # reverse character stack, concatenate to string, and update global
        self.ret = min(self.ret, ''.join(reversed(self.stack))) if self.ret \
          else ''.join(reversed(self.stack))
        self.stack.pop()
        return
      if node.left:
        recurse(node.left)
      if node.right:
        recurse(node.right)
      self.stack.pop()

    recurse(root)

    return self.ret

