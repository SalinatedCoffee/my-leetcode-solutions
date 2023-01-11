class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    # sort points by first element
    points.sort()
    arrows = 0
    # set initial overlap range
    overlap = [points[0][0], points[0][1]]

    for point in points:
      # if lower bound in overlap range
      if overlap[0] <= point[0] <= overlap[1]:
        # update overlap range accordingly
        overlap[0] = point[0]
        if point[1] < overlap[1]:
          overlap[1] = point[1]
      else:
        arrows += 1
        # set new overlap range
        overlap[0], overlap[1] = point[0], point[1]

    # check and update last group of balloons
    if overlap[0] <= point[0] <= overlap[1]:
      arrows += 1

    return arrows

