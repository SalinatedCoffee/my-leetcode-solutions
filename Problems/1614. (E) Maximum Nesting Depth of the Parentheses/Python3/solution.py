class Solution:
  def maxDepth(self, s: str) -> int:
    # emulate stack

    ret, cur = 0, 0
    for c in s:
      if c == '(':
        cur += 1
        ret = max(ret, cur)
      elif c == ')':
        cur -= 1
    
    return ret

