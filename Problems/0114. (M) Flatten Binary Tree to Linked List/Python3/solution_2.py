class Solution:
  def flatten(self, root: Optional[TreeNode]) -> None:
    # modified Morris traversal
    
    pred = TreeNode()
    cur = root
    while cur:
      if cur.left:
        # find the rightmost leaf in the left subtree
        prev = cur.left
        while prev.right:
          prev = prev.right
        # link right subtree to the right side of the leaf found in the previous step
        prev.right = cur.right
        # set left subtree as right
        cur.right = cur.left
        # properly terminate left side
        cur.left = None
      # move on to next node
      cur = cur.right

