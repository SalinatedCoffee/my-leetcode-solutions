class Solution:
  def tree2str(self, root: Optional[TreeNode]) -> str:
    # recursive DFS (NLR traversal)

    def dfs(node):
      l, r = "", ""
      if node.left is not None:
        l = f'({dfs(node.left)})'
      if node.right is not None:
        r = f'({dfs(node.right)})'
      if not l and r:
        l = "()"
      return f'{node.val}{l}{r}'

    return dfs(root)

