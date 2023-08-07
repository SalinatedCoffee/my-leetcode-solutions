class Solution:
  # top-down dynamic programming (memoization)

  def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

    return self.recurse(1, n)
  
  
  @cache
  def recurse(self, l, h):
    # returns list of all valid BSTs consisting of nodes in range [l, h]
    if l > h:
      return [None]
    if l == h:
      return [TreeNode(l)]
    ret = []
    for i in range(l, h+1):
      left = self.recurse(l, i-1)
      right = self.recurse(i+1, h)
      for l_st in left:
        for r_st in right:
          c_rt = TreeNode(i, l_st, r_st)
          ret.append(c_rt)

    return ret

