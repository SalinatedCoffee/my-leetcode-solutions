class Solution:
  def postorder(self, root: 'Node') -> List[int]:
    # recursive postorder traversal

    self.ret = []

    if root is None:
      return self.ret

    def recurse(node):
      for child in node.children:
        if child is not None:
          recurse(child)
      self.ret.append(node.val)

    recurse(root)

    return self.ret

