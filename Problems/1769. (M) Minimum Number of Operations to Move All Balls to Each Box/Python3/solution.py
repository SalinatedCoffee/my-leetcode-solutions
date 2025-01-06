class Solution:
  def minOperations(self, boxes: str) -> List[int]:
    # pre/suffix sums

    n = len(boxes)
    res = [0] * n
    # compute total distance between each box and all balls to its left
    balls, distance = 0, 0
    for i in range(n):
      distance += balls
      res[i] = distance
      if boxes[i] == '1':
        balls += 1
    # compute total distance between each box and all balls to its right
    balls, distance = 0, 0
    for i in range(n-1, -1, -1):
      distance += balls
      res[i] += distance
      if boxes[i] == '1':
        balls += 1

    return res

