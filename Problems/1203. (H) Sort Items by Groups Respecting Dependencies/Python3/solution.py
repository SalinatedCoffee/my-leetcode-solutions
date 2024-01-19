class Solution:
  def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    # topological sort (Kahn's algorithm) on multiple graphs

    # group independent nodes in separate groups
    for i in range(n):
      if group[i] == -1:
        group[i] = m
        m += 1

    # directed graph, j in adj_n|g[i] represents edge from i to j
    # ind_n|g[i] is indegree for node/group i
    # individual nodes
    adj_n = [set() for _ in range(n)]
    ind_n = [0] * n
    # groups
    adj_g = [set() for _ in range(m)]
    ind_g = [0] * m
    # generate adjacency lists and indegrees
    for i in range(n):
      for j in beforeItems[i]:
        # nodes in same group
        if group[i] == group[j]:
          adj_n[j].add(i)
          ind_n[i] += 1
        # nodes in differrent group, where edge has not been added yet
        elif group[i] not in adj_g[group[j]]:
          adj_g[group[j]].add(group[i])
          ind_g[group[i]] += 1
    
    def t_sort(g, ind):
      # implements Kahn's algorithm
      # return topologically sorted list of graph g with indegrees ind
      ret = []
      nodes = deque()
      v = len(ind)
      for i in range(v):
        if ind[i] == 0:
          nodes.append(i)
      while nodes:
        cur = nodes.popleft()
        ret.append(cur)
        for node in g[cur]:
          ind[node] -= 1
          if ind[node] == 0:
            nodes.append(node)
      for i in range(v):
        # check for cycles
        if ind[i] > 0:
          return []
      return ret
    
    # topologically sort nodes and groups
    s_n = t_sort(adj_n, ind_n)
    s_g = t_sort(adj_g, ind_g)

    ret = []
    if len(s_n) == 0 or len(s_g) == 0:
      return ret
    
    g2n = [[] for _ in range(m)]
    # partition list of sorted nodes into groups
    for i in s_n:
      g2n[group[i]].append(i)
    
    # reorder partitions according to sorted list of groups
    for i in s_g:
      ret.extend(g2n[i])

    return ret

