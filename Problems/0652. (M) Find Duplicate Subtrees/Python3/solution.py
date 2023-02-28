class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # recursive DFS with hashing

    self.seen = set()
    self.ret = {}

    def recurse(node):
      # get string representations of subtrees recursively
      l_str = recurse(node.left) if node.left else 'n'
      r_str = recurse(node.right) if node.right else 'n'
      in_str = l_str + str(node.val) + r_str + '.'
      # no previous copy of tree rooted at node
      if in_str not in self.seen:
        self.seen.add(in_str)
      # duplicate not yet added to result pool
      elif in_str not in self.ret:
        self.ret[in_str] = node
      return in_str

    recurse(root)

    # return values only
    return self.ret.values()

