class Solution:
  def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
    # greedy with binary search

    n = len(obstacles)
    ret = [1] * n

    # lis[i] is smallest value of last obstacle in courses that are i long
    lis = []

    for i, h in enumerate(obstacles):
      idx = bisect.bisect_right(lis, h)
      if idx == len(lis):
        lis.append(h)
      else:
        lis[idx] = h
      ret[i] = idx + 1
    
    return ret

