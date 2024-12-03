class Solution:
  def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
    # eulerian path on directed graph using recursive postorder DFS

    adj = defaultdict(list)
    deg = defaultdict(int)
    for u, v in pairs:
      adj[u].append(v)
      deg[u] += 1
      deg[v] -= 1
    
    res = []
    
    # traverse node using postorder DFS, using the adjacency list to remove traversed edges
    # so that we do not have to explicitly track visited edges
    def DFS(node):
      while adj[node]:
        DFS(adj[node].pop())
      res.append(node)

    # find node to start traversal
    source = -1
    for node in deg.keys():
      if deg[node] == 1:
        source = node
        break
    if source == -1:
      source = pairs[0][0]
    
    # traverse graph, and reverse eulerian path to preserve order of elements in pairs
    DFS(source)
    res.reverse()

    return [[res[i-1], res[i]] for i in range(1, len(res))]

