class Solution:
  def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    # greedy algorithm with sorting

    n = len(points)
    points.sort()
    ret = -1
    for i in range(1, n):
      ret = max(ret, points[i][0] - points[i-1][0])

    return ret

