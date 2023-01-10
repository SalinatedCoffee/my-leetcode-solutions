# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
  def __init__(self, root: Optional[TreeNode]):
    # index of current node
    self._current = 0
    # values of all nodes traversed inorder
    self._vals = []

    # just do all computations during initialization
    cur = root
    stack = []
    while True:
      # look at left subtree first
      if cur is not None:
        stack.append(cur)
        cur = cur.left
      # left subtree empty, pop from stack, record value,
      # then look at right subtree
      elif stack:
        cur = stack.pop()
        self._vals.append(cur.val)
        cur = cur.right
      # left subtree empty and no items in stack
      else:
        break

  def next(self) -> int:
    if self.hasNext():
      ret = self._vals[self._current]
      self._current += 1
      return ret

  def hasNext(self) -> bool:
    if self._current < len(self._vals):
      return True
    return False
        
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

