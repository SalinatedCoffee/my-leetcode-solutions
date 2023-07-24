class Solution:
  # top-down dynamic programming (memoization)

  def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
    # sanity check
    if not n % 2:
      return []

    return self.recurse(n)
  
  # memoize return value of recurse(i)
  @cache
  def recurse(self, n):
    if n == 1:
      return [TreeNode()]
    
    ret = []
    # generate trees for all splits...
    for i in range(1, n, 2):
      l = self.recurse(i)
      r = self.recurse(n-i-1)
      # ...and for all possible subtree pairs
      for l_s in l:
        for r_s in r:
          root = TreeNode(0, l_s, r_s)
          ret.append(root)
    
    return ret

