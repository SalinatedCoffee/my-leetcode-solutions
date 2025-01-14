class Solution:
  def canBeValid(self, s: str, locked: str) -> bool:
    # greedy algorithm using simulated stack

    # sanity check
    n = len(s)
    if n % 2 == 1:
      return False
    
    stack = 0
    wildcards = 0
    for i in range(n):
      c, l = s[i], locked[i]
      if l == '0':
        wildcards += 1
      elif c == '(':
        stack += 1
      else:
        if stack > 0:
          stack -= 1
        elif wildcards > 0:
          wildcards -= 1
        else:
          return False
    
    unmatched = 0
    for i in range(n-1, -1, -1):
      c, l = s[i], locked[i]
      if l == '0':
        unmatched -= 1
        wildcards -= 1
      elif c == '(':
        unmatched += 1
        stack -= 1
      elif c == ')':
        unmatched -= 1
      if unmatched > 0:
        return False
      if wildcards == 0 and stack == 0:
        break

    # if stack is not empty at this point, s cannot be balanced
    return False if stack > 0 else True

