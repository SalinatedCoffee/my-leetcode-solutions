class Solution:
  def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    # iterative DFS with heap indices

    widths = {}
    nodes = []
    # (node, depth, heap index)
    nodes.append((root, 1, 1))
    while nodes:
      cur, d, i = nodes.pop()
      if d not in widths:
        widths[d] = [i, i]
      else:
        widths[d][0] = min(widths[d][0], i)
        widths[d][1] = max(widths[d][1], i)
      if cur.left:
        nodes.append((cur.left, d+1, 2*i))
      if cur.right:
        nodes.append((cur.right, d+1, 2*i+1))
    
    ret = 0
    for w in widths.values():
      ret = max(ret, w[1]-w[0]+1)
    return ret

