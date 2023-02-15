class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    # sort points by first element
    points.sort()
    arrows = 0
    # set initial overlap bound
    upper = points[0][1]

    for point in points:
      # current balloon overlaps bound
      if point[0] <= upper:
        # if upper bound of current balloon also within overlap bound
        if point[1] < upper:
          upper = point[1]
      else:
        arrows += 1
        # set new overlap bound
        upper = point[1]

    # update last group of balloons
    if points[-1][0] <= upper:
      arrows += 1

    return arrows

