class Solution:
  def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    # topological sort

    def build_graph(cond):
      # build directed graph using cond
      # return adjacency list of graph and indegrees of nodes
      # use sets to store destination nodes since edges in cond are not guaranteed to be unique
      ret = [set() for _ in range(k)]
      for u, v in cond:
        ret[u-1].add(v-1)

      indeg = [0] * k
      for out in ret:
        for v in out:
          indeg[v] += 1

      return ret, indeg
    
    def topo_sort(adj, indeg):
      # perform topological sort on graph adj with indegrees indeg
      # return list of topologically sorted nodes
      nodes = deque()
      for i in range(k):
        if indeg[i] == 0:
          nodes.append(i)
      
      ret = []
      while nodes:
        node = nodes.popleft()
        ret.append(node+1)
        for d in adj[node]:
          indeg[d] -= 1
          if indeg[d] == 0:
            nodes.append(d)
      
      return ret
    
    # build graphs for row and column conditions and topologically sort them
    adj, indeg = build_graph(rowConditions)
    rows = topo_sort(adj, indeg)
    adj, indeg = build_graph(colConditions)
    cols = topo_sort(adj, indeg)
    # row or column conditions can't be sorted by topological sort
    if len(rows) != k or len(cols) != k:
      return []
    ret = [[0]*k for _ in range(k)]
    # map node value to its column number
    ntoc = {cols[i]: i for i in range(k)}
    # populate matrix
    for i in range(k):
      ret[i][ntoc[rows[i]]] = rows[i]

    return ret

