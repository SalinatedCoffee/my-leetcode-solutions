class Solution:
  def longestZigZag(self, root: Optional[TreeNode]) -> int:
    # recursive DFS

    def dfs(node, l, r):
      return 0 if node == None else max(
        max(l, r),
          max(dfs(node.left, r+1, 0), dfs(node.right, 0, l+1)))

    return dfs(root, 0, 0)

