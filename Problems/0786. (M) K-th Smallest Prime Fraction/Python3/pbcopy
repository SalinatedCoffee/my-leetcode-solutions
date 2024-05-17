class Solution:
  def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    # binary search

    n = len(arr)
    # initial search space
    l, r = 0, 1
    while l < r:
      m = (l + r) / 2
      # largest fraction seen, number of fractions smaller than m,
      # index of numerator, index of denominator
      max_val, count, nm, dm = 0, 0, 0, 0
      j = 1
      # count number of fractions smaller than m
      for i in range(n - 1):
        while j < n and arr[i] >= m * arr[j]:
          j += 1
        count += (n - j)
        if j == n:
          break
        val = arr[i] / arr[j]
        if val > max_val:
          max_val, nm, dm = val, i, j
      # if fraction count is exactly k, fraction has been found
      if count == k:
        return [arr[nm], arr[dm]]
      # if count is larger than k, fraction is in lower half
      elif count > k:
        r = m
      # otherwise, fraction is in upper half
      else:
        l = m

    # given problem constraints, this line is never reached
    return []

