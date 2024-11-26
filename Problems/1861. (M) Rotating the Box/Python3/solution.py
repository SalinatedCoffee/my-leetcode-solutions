class Solution:
  def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
    # two pointer

    m, n = len(box), len(box[0])
    # rotate box as specified
    res = [[None] * m for _ in range(n)]
    # transpose box...
    for i in range(n):
      for j in range(m):
        res[i][j] = box[j][i]
    # ...and then reverse each row
    for i in range(n):
      res[i].reverse()
    
    # apply effects of gravity to each column of rotated box
    for j in range(m):
      # index of bottom-most empty cell of current column
      h = n-1
      for i in range(n-1, -1, -1):
        if res[i][j] == '#':
          res[i][j] = '.'
          res[h][j] = '#'
          h -= 1
        if res[i][j] == '*':
          h = i-1

    return res

