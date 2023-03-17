class Solution:
  # recursive solution
  def isSymmetric(self, root: TreeNode) -> bool:
    return self.recurse(root.left, root.right)
  
  def recurse(self, left, right):
    # base cases
    if not left and not right:
      return True
    if not left or not right:
      return False
    
    # check current pair and compare recursively
    return left.val == right.val and
           self.recurse(left.left, right.right) and
           self.recurse(left.right, right.left) 

