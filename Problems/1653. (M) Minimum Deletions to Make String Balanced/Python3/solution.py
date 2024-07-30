class Solution:
  def minimumDeletions(self, s: str) -> int:
    # prefix sums
    
    n = len(s)
    # pre[i] is number of 'a's in s[:i]
    pre = [0] * (n+1)
    for i in range(1, n+1):
      pre[i] = pre[i-1] + (1 if s[i-1] == 'a' else 0)
    
    ret = float('inf')
    for i in range(n+1):
      ret = min(ret, i - 2*pre[i] + pre[-1])

    return ret

