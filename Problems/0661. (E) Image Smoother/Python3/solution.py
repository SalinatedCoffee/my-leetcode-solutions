class Solution:
  def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    # brute force

    m, n = len(img), len(img[0])
    ret = [[0]*n for _ in range(m)]

    def filter(y, x):
      tot, c = 0, 0
      for i in range(max(0, y-1), min(m, y+2)):
        for j in range(max(0, x-1), min(n, x+2)):
          tot += img[i][j]
          c += 1

      return tot // c
    
    for i in range(m):
      for j in range(n):
        ret[i][j] = filter(i, j)

    return ret

