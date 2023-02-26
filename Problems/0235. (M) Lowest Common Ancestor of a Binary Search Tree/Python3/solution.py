class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # binary search tree, return first node with value between p and q
    
    nodes = []
    nodes.append(root)
    l, h = min(p.val, q.val), max(p.val, q.val)
    # iterative DFS
    while nodes:
      cur = nodes.pop()
      if (l <= cur.val <= h):
        return cur
      if cur.right:
        nodes.append(cur.right)
      if cur.left:
        nodes.append(cur.left)
    
    # this line will never execute given constraints on p and q
    return None

