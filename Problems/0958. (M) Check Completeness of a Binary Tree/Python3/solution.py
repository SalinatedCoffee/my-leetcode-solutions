class Solution:
  def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
    # recursive DFS

    def count(root):
      # recursively count nodes in tree
      if not root:
        return 0
      return 1 + count(root.left) + count(root.right)

    def recurse(node, i, n):
      # recursively check if left and right subtrees are complete
      if not node:
        return True
      if i >= n:
        return False
      return recurse(node.left, 2*i+1, n) and \
             recurse(node.right, 2*i+2, n)

    return recurse(root, 0, count(root))
    
