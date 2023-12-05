class Solution:
  def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
    # simulation using math

    n = len(points)
    ret = 0
    for i in range(1, n):
      x, y = points[i]
      px, py = points[i-1]
      ret += max(abs(x - px), abs(y - py))
    
    return ret
   
