class Solution:
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    # BFS, treat node as 2 nodes colored either red or blue

    # sanity check
    if n == 1:
      return [0]

    # 0 for red, 1 for blue
    adj = [[[],[]] for _ in range(n)]
    for u, v in redEdges:
      adj[u][1].append(v)
    for u, v in blueEdges:
      adj[u][0].append(v)
    
    answer = [float('inf')] * n
    answer[0] = 0

    visited = [[0, 0] for _ in range(n)]
    nodes = deque()
    # add all outgoing edges from 0 regardless of color
    for i in adj[0][0]:
      nodes.append((i,1,1))
    for i in adj[0][1]:
      nodes.append((i,0,1))

    while nodes:
      cur, p_col, d = nodes.popleft()
      n_col = p_col ^ 1
      answer[cur] = d if d < answer[cur] else answer[cur]
      if visited[cur][p_col]:
        continue
      visited[cur][p_col] = 1
      for n in adj[cur][p_col]:
        nodes.append((n, n_col, d+1))
    
    return [-1 if x == float('inf') else x for x in answer]

