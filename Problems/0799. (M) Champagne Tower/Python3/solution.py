class Solution:
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    # simulation

    # generate pyramid of 'glasses'
    g = [[0]*i for i in range(1, query_row+3)]
    g[0][0] = poured
    for row in range(query_row+1):
      for col in range(row+1):
        # for each glass, determine the flow-through volume into the 2 glasses in the next row
        q = (g[row][col] - 1) / 2
        if q > 0:
          g[row+1][col] += q
          g[row+1][col+1] += q

    # g itself stores the volume that flows into a glass, and not the actual volume held by it
    # so if value is larger than what a glass can hold, return 1
    return min(1, g[query_row][query_glass])

