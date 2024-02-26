class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # stacks

    stack_p = [p]
    stack_q = [q]
    while stack_p:
      cur_p = stack_p.pop()
      cur_q = stack_q.pop()
      if cur_p is None and cur_q is None:
        continue
      elif cur_p is None or cur_q is None:
        return False
      else:
        if cur_p.val != cur_q.val:
          return False
        stack_p.append(cur_p.right)
        stack_p.append(cur_p.left)
        stack_q.append(cur_q.right)
        stack_q.append(cur_q.left)

    return True

