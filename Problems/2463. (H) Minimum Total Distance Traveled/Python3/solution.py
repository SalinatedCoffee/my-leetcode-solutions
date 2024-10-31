class Solution:
  def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
    # top-down dynamic programming (memoization) on sorted lists

    robot.sort()
    factory.sort(key=lambda x: x[0])
    # flatten list of factories, repeating their positions by their capacities
    factory = [pos for pos, cap in factory for _ in range(cap)]
    m, n = len(robot), len(factory)
    # dp[i][j] is minimum distance moved for robot[i:] and factory[j:]
    dp = [[-1]*(n+1) for _ in range(m+1)]

    def recurse(r, f):
      # base cases
      if r == m:
        return 0
      if f == n:
        return float('inf')
      if dp[r][f] != -1:
        return dp[r][f]
      # repair robot at current factory
      dp[r][f] = abs(robot[r] - factory[f]) + recurse(r+1, f+1)
      # skip current factory
      dp[r][f] = min(dp[r][f], recurse(r, f+1))

      return dp[r][f]

    return recurse(0, 0)

