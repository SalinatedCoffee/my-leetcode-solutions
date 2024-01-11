class Solution:
  def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
    # recursive DFS

    def dfs(node, s, l):
      # return maximum ancestor difference for subtree rooted at node
      #   and predecessor minimum and maximum values are s and l respectively
      ret = max(abs(node.val - s), abs(node.val - l))
      n_s, n_l = min(s, node.val), max(l, node.val)
      if node.left:
        ret = max(ret, dfs(node.left, n_s, n_l))
      if node.right:
        ret = max(ret, dfs(node.right, n_s, n_l))

      return ret

    return dfs(root, root.val, root.val)

