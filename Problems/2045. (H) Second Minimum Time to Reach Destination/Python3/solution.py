class Solution:
  def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
    # iterative BFS

    # convert list of edges to adjacency list
    adj = [[] for _ in range(n+1)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    # list of shortest and second shortest distances from node 1 to others
    d1, d2 = [-1] * (n+1), [-1] * (n+1)
    d1[1] = 0
    nodes = deque([(1, 1)])
    while nodes:
      cur, visits = nodes.popleft()
      # use appropriate elapsed time depending on number of visits to cur
      t = d1[cur] if visits == 1 else d2[cur]
      # if current light is red, add time required for it to change to green
      if t // change % 2 == 1:
        t = change * (t // change + 1) + time
      # otherwise, immediately travel to neighboring node
      else:
        t += time
      for nxt in adj[cur]:
        if d1[nxt] == -1:
          d1[nxt] = t
          nodes.append((nxt, 1))
        # if neighbor is visited a second time
        # and the elapsed time for the visit is not equal to the first visit
        elif d2[nxt] == -1 and d1[nxt] != t:
          if nxt == n:
            return t
          d2[nxt] = t
          nodes.append((nxt, 2))

    # given problem constraints, this line will never be reached
    return 0

