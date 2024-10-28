class Solution:
  def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    # recursion

    # check roots
    if root1 is None:
      if root2:
        return False
    if root2 is None:
      if root1:
        return False
      return True
    if root1.val != root2.val:
      return False
    
    # match children of roots
    pairs = []
    for i in [root1.left, root1.right]:
      for j in [root2.left, root2.right]:
        if i and j and i.val == j.val:
          pairs.append((i, j))
    
    # determine whether all children have been paired
    count = 0
    count += 1 if root1.left else 0
    count += 1 if root1.right else 0
    count += 1 if root2.left else 0
    count += 1 if root2.right else 0
    if len(pairs) * 2 != count:
      return False
    
    # recurse
    res = True
    for i, j in pairs:
      res &= self.flipEquiv(i, j)
    
    return res
        
