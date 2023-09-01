class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    # greedy

    max_reach = defaultdict(int)
    # precompute maximum watering range starting at each position
    for i, r in enumerate(ranges):
      max_reach[max(0, i-r)] = max(max_reach[max(0, i-r)], i+r)

    ret = 0
    # furthest watering range for current tap / next tap
    cur_reach, nxt_reach = 0, 0
    for i in range(n+1):
      if i > nxt_reach:
        return -1
      if i > cur_reach:
        ret += 1
        cur_reach = nxt_reach
      nxt_reach = max(nxt_reach, max_reach[i])

    return ret

