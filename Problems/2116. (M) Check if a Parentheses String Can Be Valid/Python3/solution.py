class Solution:
  def canBeValid(self, s: str, locked: str) -> bool:
    # greedy algorithm using stacks

    # sanity check
    n = len(s)
    if n % 2 == 1:
      return False
    
    stack = []
    wildcards = []
    for i in range(n):
      c, l = s[i], locked[i]
      if l == '0':
        wildcards.append(i)
      elif c == '(':
        stack.append(i)
      else:
        if stack:
          stack.pop()
        elif wildcards:
          wildcards.pop()
        else:
          return False
    
    # pair unmatched open parentheses with wildcards if possible
    while stack and wildcards and stack[-1] < wildcards[-1]:
      stack.pop()
      wildcards.pop()

    return False if stack else True

