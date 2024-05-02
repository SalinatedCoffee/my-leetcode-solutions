class Solution:
  def findRotateSteps(self, ring: str, key: str) -> int:
    # top-down dynamic programming (memoization)

    m, n = len(ring), len(key)
    # preprocess ring for fast access to indices of next char
    ctoi = defaultdict(list)
    for i, c in enumerate(ring):
      ctoi[c].append(i)

    @cache
    def recurse(idx, north):
      # return minimum number of steps to match key[idx:]
      # when ring[north] is at the 12:00 position
      if idx == n:
        return 0
      ret = float('inf')
      for n_pos in ctoi[key[idx]]:
        dist = min(abs(north - n_pos), m - abs(north - n_pos))
        ret = min(ret, dist + 1 + recurse(idx+1, n_pos))

      return ret

    return recurse(0, 0)

