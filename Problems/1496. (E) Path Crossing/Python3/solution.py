class Solution:
  def isPathCrossing(self, path: str) -> bool:
    # brute force using sets

    x, y = 0, 0
    history = defaultdict(set)
    history[x].add(y)
    for d in path:
      match d:
        case 'N':
          y += 1
        case 'S':
          y -= 1
        case 'E':
          x += 1
        case 'W':
          x -= 1
      if x in history and y in history[x]:
        return True
      history[x].add(y)
    
    return False

