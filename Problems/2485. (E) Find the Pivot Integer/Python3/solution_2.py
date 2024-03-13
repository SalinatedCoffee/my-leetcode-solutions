class Solution:
  def pivotInteger(self, n: int) -> int:
    # binary search using math

    # given potential pivot x, compute sum of left and right sides
    lhs, rhs = lambda x: x*(x+1)//2, lambda x: (n-x+1)*(n-x+2)//2+(x-1)*(n-x+1)
    l, h = 1, n
    while l <= h:
      m = l + (h - l) // 2
      if lhs(m) == rhs(m):
        return m
      # left side is larger, search left side for pivot
      if lhs(m) > rhs(m):
        h = m - 1
      # right side is larger
      else:
        l = m + 1
    
    return -1

