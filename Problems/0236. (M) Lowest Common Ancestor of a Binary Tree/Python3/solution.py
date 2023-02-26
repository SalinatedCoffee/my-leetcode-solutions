class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # get paths from root to p and q then compare

    # recursively build path from node to tgt
    def dfs(node, path, tgt):
      if not node:
        return False
      path.append(node)
      if node.val == tgt:
        return True
      if dfs(node.left, path, tgt) or dfs(node.right, path, tgt):
        return True
      path.pop()
      return False
    
    # get paths from root to p and q
    path_p, path_q = [], []
    dfs(root, path_p, p.val)
    dfs(root, path_q, q.val)

    # compare both paths
    for i in range(min(len(path_p), len(path_q))):
      if path_p[i] != path_q[i]:
        return path_p[i-1]

    return path_p[i]

