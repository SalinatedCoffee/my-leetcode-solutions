# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
      # preorder is N -> L -> R
      # recursive solution
      ret = []
      def helper(root, ret):
        if root is not None:
          ret.append(root.val)
          helper(root.left, ret)
          helper(root.right, ret)
      
      helper(root, ret)
      return ret

