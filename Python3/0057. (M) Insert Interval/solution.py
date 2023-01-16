class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    # add the new interval to interval list, sort by first element

    # sanity check
    if newInterval is None:
      return intervals
    if intervals is None:
      return intervals
        
    # append new interval to intervals
    intervals.append(newInterval)

    # sort intervals by first element, in-place
    intervals.sort()
    ret = []
    new_i = intervals[0]
    ret.append(new_i)
        
    # merge intervals (problem #56)
    for interval in intervals:
      if new_i[1] >= interval[0]:
        new_i[1] = max(new_i[1], interval[1])
      else:
        new_i = interval
        ret.append(new_i)
                
    return ret

