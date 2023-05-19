class Solution:
  def isBipartite(self, graph: List[List[int]]) -> bool:
    # iterative DFS

    n = len(graph)
    coloring = [None] * n
    for i in range(n):
      if coloring[i] is not None:
        continue

      nodes = [(i, True)]
      while nodes:
        cur, color = nodes.pop()
        if coloring[cur] is not None:
          if coloring[cur] != color:
            return False
          continue
        coloring[cur] = color
        
        color ^= True
        for nxt in graph[cur]:
          nodes.append((nxt, color))

    return True

