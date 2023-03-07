class Solution:
  def countBits(self, n: int) -> List[int]:
    # memoize previous results
    
    ret = []
    for i in range(n+1):
      ret.append(ret[i//2] + i%2 if i else 0)
    
    return ret

