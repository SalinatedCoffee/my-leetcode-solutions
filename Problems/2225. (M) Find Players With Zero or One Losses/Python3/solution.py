class Solution:
  def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    # dictionary

    losses = {}
    for w, l in matches:
      if w not in adj:
        losses[w] = 0
      if l not in adj:
        losses[l] = 0
      adj[l] += 1
    
    ret = [[],[]]
    for p in sorted(losses.keys()):
      if adj[p] < 2:
        ret[losses[p]].append(p)

    return ret

