class Solution:
  def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # brute force DFS

    def dfs(node, leaves):
      if node.left:
        dfs(node.left, leaves)
      if node.right:
        dfs(node.right, leaves)
      if not node.left and not node.right:
        leaves.append(node.val)
    
    a, b = [], []
    dfs(root1, a)
    dfs(root2, b)

    for i, j in zip(a, b):
      if i != j:
        return False

    return len(a) == len(b)

