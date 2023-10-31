class Solution:
  def paintWalls(self, cost: List[int], time: List[int]) -> int:
    # top-down dynamic programming (memoization)

    n = len(cost)

    @cache
    # recurse(i, j) returns the minimum cost to paint j walls
    #   using cost[i:] and time[i:]
    def recurse(i, rem):
      if rem <= 0:
        return 0
      if i == n:
        return float('inf')
      hire = cost[i] + recurse(i+1, rem-1-time[i])
      skip = recurse(i+1, rem)
      return min(hire, skip)
    
    return recurse(0, n)

