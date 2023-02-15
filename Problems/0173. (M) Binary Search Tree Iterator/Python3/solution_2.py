# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
  def __init__(self, root: Optional[TreeNode]):
    # current node
    self._current = root
    # values of all nodes traversed inorder
    self._stack = []

    # descend furthest down left subtree
    while self._current:
      self._stack.append(self._current)
      self._current = self._current.left

  def next(self) -> int:
    while True:
      # attempt to traverse left subtree
      if self._current:
        self._stack.append(self._current)
        self._current = self._current.left
      # if left subtree is None, pop from stack and look at right subtree
      # return value of popped node
      elif self._stack:
        cur = self._stack.pop()
        self._current = cur.right
        return cur.val

  def hasNext(self) -> bool:
    # node cannot have next inorder if tree is empty
    # tree is empty if left subtree is None and no parent node to backtrack to
    if not self._current and not self._stack:
      return False
    return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
