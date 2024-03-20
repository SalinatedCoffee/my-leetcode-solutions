class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # single pass solution
    
    n = len(intervals)
    i = 0
    ret = []

    # process all non-overlapping intervals to the left of newInterval
    while i < n and intervals[i][1] < newInterval[0]:
      ret.append(intervals[i])
      i += 1
    # process all overlapping intervals
    while i < n and newInterval[1] >= intervals[i][0]:
      newInterval[0] = min(newInterval[0], intervals[i][0])
      newInterval[1] = max(newInterval[1], intervals[i][1])
      i += 1
    ret.append(newInterval)
    # process all non-overlapping intervals to the right
    while i < n:
      ret.append(intervals[i])
      i += 1

    return ret

