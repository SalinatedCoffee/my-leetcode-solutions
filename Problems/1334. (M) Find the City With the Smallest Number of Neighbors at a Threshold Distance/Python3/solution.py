class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    # Floyd-Warshall

    # initialize distances
    dists = [[float('inf')]*n for _ in range(n)]
    for u, v, w in edges:
      dists[u][u] = 0
      dists[v][v] = 0
      dists[u][v] = w
      dists[v][u] = w
    
    # relax edges
    for i in range(n):
      for j in range(n):
        for k in range(n):
          dists[j][k] = min(dists[j][k], dists[j][i] + dists[i][k])

    # find valid node with largest label
    ret, min_reachable = 0, 100
    for i in range(n):
      valid = 0
      for j in range(n):
        if dists[i][j] <= distanceThreshold:
          valid += 1
      if valid <= min_reachable:
        ret, min_reachable = i, valid

    return ret

