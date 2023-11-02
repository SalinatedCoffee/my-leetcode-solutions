class Solution:
  def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
    # recursive postorder (LRN) tree traversal

    self.ret = 0

    def recurse(node):
      tot, size = node.val, 1
      if node.left:
        l_tot, l_size = recurse(node.left)
        tot += l_tot
        size += l_size
      if node.right:
        r_tot, r_size = recurse(node.right)
        tot += r_tot
        size += r_size
      if node.val == tot // size:
        self.ret += 1
      
      return tot, size
    
    recurse(root)

    return self.ret

