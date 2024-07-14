class Solution:
  def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
    # stack with sorted list
    
    n = len(positions)
    # sort robots in ascending order of their positions
    idx = [i for i in range(n)]
    idx.sort(key=lambda x: positions[x])

    stack = []
    for i in idx:
      if not stack:
        stack.append(i)
      else:
        # simulate collisions until none happens
        while stack and directions[stack[-1]] == 'R' and directions[i] == 'L':
          d = healths[stack[-1]] - healths[i]
          # adjust healths accordingly
          if d > 0:
            healths[stack[-1]] -= 1
            healths[i] = 0
          elif d == 0:
            healths[stack[-1]] = 0
            healths[i] = 0
          elif d < 0:
            healths[stack[-1]] = 0
            healths[i] -= 1
          # remove robots with 0 health
          if healths[stack[-1]] == 0:
            stack.pop()
          if healths[i] == 0:
            break
        # if current robot has survived
        if healths[i]:
          stack.append(i)

    return list(filter(lambda x: x, healths))

