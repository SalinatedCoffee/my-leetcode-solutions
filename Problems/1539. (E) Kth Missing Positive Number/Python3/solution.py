class Solution(object):
  def findKthPositive(self, arr, k):
    # binary search based on number of missing integers at element

    l, h = 0, len(arr) - 1
    while l <= h:
      m = (l + h) // 2
      if arr[m] - m - 1 < k:
        l = m + 1
      else:
        h = m - 1

    return l + k

