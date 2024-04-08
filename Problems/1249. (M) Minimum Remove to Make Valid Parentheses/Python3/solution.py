class Solution:
  def minRemoveToMakeValid(self, s: str) -> str:
    # greedy with suffix count

    n = len(s)
    # count number of close parentheses in suffix
    suf = [0] * n
    count = 0
    for i in range(n-1, -1, -1):
      count += 1 if s[i] == ')' else 0
      suf[i] = count
    
    # greedily match open parentheses
    stack = []
    o = 0
    for i in range(n):
      if s[i] == '(':
        # if this open parentheses can be closed
        if suf[i] - o:
          stack.append(s[i])
          o += 1
      elif s[i] == ')':
        # if there are open parentheses that can be closed
        if o:
          stack.append(s[i])
          o -= 1
      else:
        stack.append(s[i])

    # reconstruct string
    return ''.join(stack)

