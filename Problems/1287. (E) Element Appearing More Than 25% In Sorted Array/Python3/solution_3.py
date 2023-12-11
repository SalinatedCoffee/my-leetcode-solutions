class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    # binary search

    n = len(arr)

    # sanity check
    if n == 1:
      return arr[0]
    
    # retrieve elements at boundaries
    tgt = n // 4
    can = set([arr[0], arr[-1]])
    for i in range(1, 4):
      can.add(arr[tgt*i-1])
      can.add(arr[tgt*i])
    # count each candidate in arr
    thold = n / 4
    for c in can:
      l, h = bisect_left(arr, c), bisect_right(arr, c)
      if h - l > thold:
        return c

    return -1

