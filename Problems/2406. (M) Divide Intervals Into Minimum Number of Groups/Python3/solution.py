class Solution:
  def minGroups(self, intervals: List[List[int]]) -> int:
    # line sweep without sorting

    # initialize sweep interval
    l, h = min(intervals, key=lambda x: x[0]), max(intervals, key=lambda x: x[1])

    # count beginning and end of each interval
    counts = [0] * (h + 2)
    for i, j in intervals:
      counts[i] += 1
      counts[j+1] -= 1
    
    # determine maximum number of overlapping intervals
    overlap = 0
    max_overlap = 0
    for i in range(l, h+1):
      overlap += counts[i]
      max_overlap = max(max_overlap, overlap)

    return max_overlap

