class Solution:
  def countBits(self, n: int) -> List[int]:
    # memoize previous results
    
    ret = [0] * (n+1)
    for i in range(n+1):
      ret[i] = ret[i//2] + i%2 if i else 0
    
    return ret

