class Solution:
  def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # recursive DFS

    def recurse(left, right, depth=0):
      if left is None:
        return
      if depth % 2 == 0:
        left.val, right.val = right.val, left.val
      recurse(left.left, right.right, depth + 1)
      recurse(left.right, right.left, depth + 1)
    
    recurse(root.left, root.right)

    return root

