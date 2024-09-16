class Solution:
  def findMinDifference(self, timePoints: List[str]) -> int:
    # sorting

    n = len(timePoints)
    # sort time points in ascending order
    timePoints.sort()
    # convert all time points into minutes
    timePoints = list(map(lambda x: int(x[:2])*60 + int(x[-2:]), timePoints))
    # determine smallest difference
    res = 60*24
    for i in range(n-1):
      res = min(res, timePoints[i+1] - timePoints[i])
    res = min(res, 60*24 - timePoints[-1] + timePoints[0])

    return res

