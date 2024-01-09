class Solution:
  def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    # brute force DFS

    ret = 0
    nodes = [root]
    while nodes:
      cur = nodes.pop()
      if not cur:
        continue
      if low <= cur.val <= high:
        ret += cur.val
      nodes.append(cur.left)
      nodes.append(cur.right)

    return ret

