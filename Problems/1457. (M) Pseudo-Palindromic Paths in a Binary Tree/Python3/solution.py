class Solution:
  def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
    # dfs with bit manipulation

    def dfs(node, d, s):
      # returns number of pseudo-palindromic paths from node to descendant leaves
      # where the parent of node has depth d
      # and the set of nodes appearing an odd number of times
      # in the path from the root to node is s
      d_n, s_n = d + 1, s ^ (1 << node.val)
      if node.left is None and node.right is None:
        if d_n % 2 == 0:
          return 1 if s_n == 0 else 0
        else:
          return 1 if s_n.bit_count() == 1 else 0
      l = dfs(node.left, d_n, s_n) if node.left else 0
      r = dfs(node.right, d_n, s_n) if node.right else 0

      return l + r

    return dfs(root, 0, 0)

