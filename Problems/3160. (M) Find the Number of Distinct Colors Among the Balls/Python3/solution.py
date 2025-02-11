class Solution:
  def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    # simulation using maps

    n = len(queries)
    # current colors of colored balls
    config = defaultdict(int)
    # number of balls of each color
    colors = defaultdict(int)
    res = []
    for i, c in queries:
      # ball has been colored before
      if i in config:
        if colors[config[i]] == 1:
          del colors[config[i]]
        else:
          colors[config[i]] -= 1
      config[i] = c
      colors[c] += 1
      res.append(len(colors))

    return res

