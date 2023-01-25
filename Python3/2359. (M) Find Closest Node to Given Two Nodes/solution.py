class Solution:
  def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
    # get length of shortest paths to all nodes from start via BFS
    def bfs(start):
      nodes = deque()
      nodes.append((start, 0))
      seen = {}
      while nodes:
        cur, steps = nodes.popleft()
        if cur in seen:
          continue
        else:
          seen[cur] = steps
        if edges[cur] != -1:
          nodes.append((edges[cur], steps+1))
      
      return seen
    
    # generate path lengths for both nodes
    n1_steps, n2_steps = bfs(node1), bfs(node2)

    min_dist = 10**5
    min_idx = -1
    for i in range(len(edges)):
      if i in n1_steps and i in n2_steps:
        # get larger of two path lengths
        max_cur = max(n1_steps[i], n2_steps[i])
        # update if length is shortest
        if max_cur < min_dist:
          min_dist = max_cur
          min_idx = i
    
    return min_idx

