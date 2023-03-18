class Solution:
  def sumNumbers(self, root: Optional[TreeNode], total=0) -> int:
    # recursive DFS

    if not root:
      return 0
    
    total *= 10
    total += root.val
    lr_sum = self.sumNumbers(root.left, total) + self.sumNumbers(root.right, total)

    return lr_sum if lr_sum else total

