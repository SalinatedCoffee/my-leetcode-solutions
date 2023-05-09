class Solution:
  def predictPartyVictory(self, senate: str) -> str:
    # double queues
    
    n = len(senate)
    r, d = deque(), deque()
    for i in range(n):
      if senate[i] == 'R':
        r.append(i)
      else:
        d.append(i)
    
    while r and d:
      r_cur, d_cur = r.popleft(), d.popleft()
      if r_cur > d_cur:
        d.append(d_cur+n)
      else:
        r.append(r_cur+n)
    
    return "Radiant" if r else "Dire"

