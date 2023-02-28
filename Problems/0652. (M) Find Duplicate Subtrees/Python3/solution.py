class Solution:
  def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # recursive DFS with hashing

    self.seen = set()
    self.ret = {}

    def recurse(node):
      # get string representations of subtrees recursively
      l_str = recurse(node.left) if node.left else 'n'
      r_str = recurse(node.right) if node.right else 'n'
      pre_str = l_str + str(node.val) + r_str + '.'
      # no previous copy of tree rooted at node
      if pre_str not in self.seen:
        self.seen.add(pre_str)
      # duplicate not yet added to result pool
      elif pre_str not in self.ret:
        self.ret[pre_str] = node
      return pre_str

    recurse(root)

    # return values only
    return self.ret.values()

