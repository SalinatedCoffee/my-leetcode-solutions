class Solution:
  def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    # stack

    ret = []
    for m in asteroids:
      keep = True
      while ret and ret[-1] > 0 and m < 0:
        if abs(ret[-1]) < abs(m):
          ret.pop()
          continue
        elif abs(ret[-1]) == abs(m):
          ret.pop()
        keep = False
        break
      if keep:
        ret.append(m)
    
    return ret

