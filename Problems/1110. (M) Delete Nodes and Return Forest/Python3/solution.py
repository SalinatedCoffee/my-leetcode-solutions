class Solution:
  def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    # recursive DFS

    # convert list to set for fast lookups
    to_delete_set = set(to_delete)
    self.ret = []

    def recurse(node, parent=None, left=True):
      if node.val not in to_delete_set and parent is None:
        self.ret.append(node)
      cur = node
      if node.val in to_delete_set:
        # mark current node as deleted
        cur = None
        # unlink from parent
        if parent:
          if left:
            parent.left = None
          else:
            parent.right = None
      if node.left:
        recurse(node.left, cur)
      if node.right:
        recurse(node.right, cur, False)

    recurse(root)

    return self.ret

