class Solution:
  def numberOfWays(self, corridor: str) -> int:
    # math

    mod = 10**9 + 7
    chairs, plants = 0, 0
    ret = 1
    for c in corridor:
      if chairs < 2:
        if c == 'S':
          chairs += 1
      else:
        if c == 'S':
          ret *= plants+1 if plants else 1
          plants = 0
          chairs = 1
        else:
          plants += 1
    
    if chairs == 0:
      return 0
    
    return ret % mod if chairs != 1 else 0

