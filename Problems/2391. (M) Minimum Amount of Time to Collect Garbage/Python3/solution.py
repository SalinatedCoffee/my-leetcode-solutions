class Solution:
  def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    # brute force

    n = len(garbage)
    # find last house for each garbage type
    TYPES = 'MPG'
    l_idx = {}
    for t in TYPES:
      for i in range(n-1, -1, -1):
        if t in garbage[i]:
          l_idx[t] = i
          break
    
    ret = 0
    # directly compute required time for each garbage type
    for t, p in l_idx.items():
      for i in range(p):
        ret += garbage[i].count(t)
        ret += travel[i]
      ret += garbage[p].count(t)
    
    return ret

