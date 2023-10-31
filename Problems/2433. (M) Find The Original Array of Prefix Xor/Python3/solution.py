class Solution:
  def findArray(self, pref: List[int]) -> List[int]:
    # boolean algebra
    
    n = len(pref)
    ret = [pref[0]]
    cur = pref[0]
    for i in range(1, n):
      temp = cur ^ pref[i]
      ret.append(temp)
      cur ^= temp
    
    return ret

