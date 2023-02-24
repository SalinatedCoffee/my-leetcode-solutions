class Solution:
  def kthSmallest(self, root: TreeNode, k: int) -> int:
    # inorder traversal with counter updates
    
    nodes = []
    cur = root
    # iterative traversal
    while True:
      if cur:
        nodes.append(cur)
        cur = cur.left
      elif nodes:
        cur = nodes.pop()
        # check and update counter appropriately
        if k == 1:
          return cur.val
        k -= 1
        cur = cur.right
      else:
        break

    # this line will never run given constraints on len(root) and k
    return -1

