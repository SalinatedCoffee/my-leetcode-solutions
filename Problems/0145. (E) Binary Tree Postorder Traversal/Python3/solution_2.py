class Solution:
  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    # iterative postorder traversal (LRN)

    # sanity check
    if root is None:
      return []

    ret = []
    nodes = []
    cur = root
    while True:
      # traverse down left as much as possible
      while cur:
        if cur.right:
          nodes.append(cur.right)
        nodes.append(cur)
        cur = cur.left
      cur = nodes.pop()
      # current node has no left child, but is not a leaf
      # traverse to its right child
      if nodes and (cur.right is nodes[-1]):
        nodes.pop()
        nodes.append(cur)
        cur = cur.right
      # current node is a leaf
      else:
        ret.append(cur.val)
        cur = None
      if not nodes:
        break

    return ret

