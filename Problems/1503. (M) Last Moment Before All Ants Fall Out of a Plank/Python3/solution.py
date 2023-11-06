class Solution:
  def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
    
    ret = 0
    if right:
      ret = n - min(right)
    if left:
      ret = max(ret, max(left))

    return ret

