class Solution:
  def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    # binary search

    # determine whether it is possible to distribute the products in q
    # to n products such that each store's stock does not exceed k
    def verify(k, q, n):
      for stock in q:
        stores = ceil(stock / k)
        if n < stores:
          return False
        n -= stores

      return True

    m = len(quantities)
    # define initial search space
    l, h = 1, max(quantities) 
    res = h
    # determine minimum value of k that would result in a valid distribution
    while l <= h:
      m = l + (h - l) // 2
      if verify(m, quantities, n) is True:
        res = m
        h = m - 1
      else:
        l = m + 1

    return res

