class Solution:
  def trap(self, height: List[int]) -> int:
    # pre/suffix maximums

    n = len(height)
    # precompute pre/suffix maximums
    # l[i] contains maximum value within height[:i+1]
    # r[i] contains maximum value within height[i:]
    l, r = [0] * n, [0] * n
    l[0] = height[0]
    for i in range(1, n):
      l[i] = max(l[i-1], height[i])
    r[-1] = height[-1]
    for i in range(n-2, -1, -1):
      r[i] = max(r[i+1], height[i])
    
    ret = 0
    # compute amount of trapped water for each column
    for i in range(n):
      ret += min(l[i], r[i]) - height[i]
    
    return ret

