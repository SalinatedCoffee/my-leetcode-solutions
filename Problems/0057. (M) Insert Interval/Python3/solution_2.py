class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # linear solution

    # sanity check
    if not intervals:
      return [newInterval]

    ret = []
    # boundary of merged interval
    lo, hi = newInterval
    # if new interval has been inserted / merge in progress
    insert, merge = False, False
    for i, j in intervals:
      # no overlap, current interval is smaller than new
      if j < newInterval[0]:
        ret.append([i, j])
      # no overlap, current interval is larger than new
      elif newInterval[1] < i:
        # if current interval is being merged or has not been inserted yet
        if merge or not insert:
          ret.append([lo, hi])
          insert = True
          merge = False
        ret.append([i, j])
      # overlap exists, merge interval
      else:
        merge = True
        lo = min(i, lo)
        hi = max(j, hi)

    # if new interval hasn't been inserted yet
    if not insert:
      ret.append([lo, hi])

    return ret

