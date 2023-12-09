class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # iterative DFS (LNR traversal)

    ret = []
    nodes = []
    cur = root
    while True:
      if cur is not None:
        nodes.append(cur)
        cur = cur.left
      elif nodes:
        cur = nodes.pop()
        ret.append(cur.val)
        cur = cur.right
      else:
        break

    return ret

