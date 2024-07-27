class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    # Floyd-Warshall
    
    alpha = len(string.ascii_lowercase)
    # value of costs[i][j] is minimum cost of converting letter i into j
    costs = [[float('inf')]*alpha for _ in range(alpha)]
    ctoi = lambda x: ord(x) - ord('a')
    for u, v, w in zip(original, changed, cost):
      # multiple edges can exist between two nodes, only add the one with smallest weight
      if costs[ctoi(u)][ctoi(v)] > w:
        costs[ctoi(u)][ctoi(v)] = w
    for i in range(alpha):
      costs[i][i] = 0
    
    # relax edges
    for i in range(alpha):
      for j in range(alpha):
        for k in range(alpha):
          if costs[j][k] > costs[j][i] + costs[i][k]:
            costs[j][k] = costs[j][i] + costs[i][k]

    # compute cost of conversion
    ret = 0
    for a, b in zip(source, target):
      if costs[ctoi(a)][ctoi(b)] == float('inf'):
        return -1
      ret += costs[ctoi(a)][ctoi(b)]

    return ret

