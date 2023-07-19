class Solution:
  def maxValue(self, events: List[List[int]], k: int) -> int:
    # top-down dynamic programming with binary search

    n = len(events)
    ev_sorted = sorted(events)
    # dp[i][j] is maximum score after i attended events out of events[j:]
    dp = [[-1] * n for _ in range(k + 1)]

    def recurse(c_idx, c):
      if c_idx == n or not c:
        return 0
      if dp[c][c_idx] != -1:
        return dp[c][c_idx]
      skip = recurse(c_idx + 1, c)
      n_idx = bisect_right(ev_sorted, ev_sorted[c_idx][1], key=lambda x: x[0])
      take = ev_sorted[c_idx][2] + recurse(n_idx, c - 1)
      dp[c][c_idx] = max(skip, take)
      
      return dp[c][c_idx]

    return recurse(0, k)

