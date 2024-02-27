class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # recursion

    ret = 0

    def recurse(node):
      l = recurse(node.left) if node.left else -1
      r = recurse(node.right) if node.right else -1
      nonlocal ret
      ret = max(ret, l+r+2)

      return max(l, r) + 1

    recurse(root)

    return ret

