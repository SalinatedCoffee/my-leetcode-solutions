class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
    # recursive DFS

    # overall max path sum
    self.max_sum = float('-inf')

    def recurse(node):
      # recursively get left and right path sums
      left_sum = recurse(node.left) if node.left else 0
      right_sum = recurse(node.right) if node.right else 0
      # see whether path sum in subtree rooted at node is larger than previous max
      self.max_sum = max(self.max_sum, left_sum+node.val+right_sum)
      ret = max(node.val+left_sum, node.val+right_sum)
      return ret if ret > 0 else 0

    recurse(root)

    return self.max_sum

