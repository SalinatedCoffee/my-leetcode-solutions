class Solution:
  def maxTwoEvents(self, events: List[List[int]]) -> int:
    # binary search with dictionary and sorting
    
    n = len(events)
    # sort events by starting time
    events.sort()
    # value of max_ev[t] is largest value among events that begin at time t or later
    max_ev = defaultdict(int)
    # populate max_ev
    cur_max = 0
    for i in range(n-1, -1, -1):
      s, e, v = events[i]
      cur_max = max(cur_max, v)
      max_ev[s] = cur_max

    # retrieve list of unique starting times
    keys = list(reversed(max_ev.keys()))
    res = 0
    # for each event, determine the largest value of a non-overlapping event
    for s, e, v in events:
      idx = bisect_left(keys, e + 1)
      s2 = -1 if idx == len(keys) else keys[idx]
      res = max(res, v + max_ev[s2])

    return res

