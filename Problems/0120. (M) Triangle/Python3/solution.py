class Solution:
  def minimumTotal(self, triangle: List[List[int]]) -> int:
    # top-down dynamic programming (memoization)

    n = len(triangle)

    @cache
    def recurse(r, c):
      # return minimum sum of values in path from triangle[0][0] to triangle[r][c]
      if r == 0:
        return triangle[0][0]
      # guaranteed that both cases never evaluate to false, sloppy but works
      return min(recurse(r-1, c) if r-1 >= c else float('inf'),
        recurse(r-1, c-1) if c > 0 else float('inf')) \
        + triangle[r][c]

    # return minimum path sum across all values in last row
    return min([recurse(n-1, c) for c in range(n)])

