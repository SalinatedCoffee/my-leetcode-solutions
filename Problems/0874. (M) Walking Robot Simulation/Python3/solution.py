class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
      # simulation

      n = len(commands)
      VEC = [(0, 1), (1, 0), (0, -1), (-1, 0)]
      obs_set = set(map(tuple, obstacles))
      # current coordinates and direction
      x, y, v = 0, 0, 0
      c = 0
      res = 0
      while c < n:
        match commands[c]:
          # change direction appropriately
          case -2:
            v = (v + 4 - 1) % 4
          case -1:
            v = (v + 1) % 4
          # incrementally try walking forward
          case _:
            dx, dy = VEC[v]
            for _ in range(commands[c]):
              if (x+dx, y+dy) in obs_set:
                break
              x += dx
              y += dy
            res = max(res, x**2+y**2)
        c += 1

      return res

