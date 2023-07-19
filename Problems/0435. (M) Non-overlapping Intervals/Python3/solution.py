class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # greedy with sorting

    n = len(intervals)
    in_sorted = sorted(intervals, key=lambda x: x[1])

    ret = 0
    k = float('-inf')
    for x, y in in_sorted:
      if x >= k:
        k = y
      else:
        ret += 1
    
    return ret

