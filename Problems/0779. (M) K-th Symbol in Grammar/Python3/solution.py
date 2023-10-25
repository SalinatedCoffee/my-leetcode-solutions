class Solution:
  def kthGrammar(self, n: int, k: int) -> int:
    # recursive binary search

    # return l-th symbol with o-1 remaining rows rooted at symbol r
    def recurse(o, l, r):
      # last row, return root
      if o == 1:
        return r
      # number of leaf nodes of tree rooted at r with o rows
      t_nodes = 2**(o-1)
      # binary search; if desired symbol is in right subtree
      if l > (t_nodes / 2):
        # determine root of right subtree based on symbol of root r and recurse
        n_r = 1 if r == 0 else 0
        return recurse(o-1, l-(t_nodes/2), n_r)
      # do the same for the other case
      else:
        n_r = 0 if r == 0 else 1
        return recurse(o-1, l, n_r)
    
    return recurse(n, k, 0)

