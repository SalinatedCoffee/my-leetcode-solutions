class Solution:
  def removeOccurrences(self, s: str, part: str) -> str:
    # stack

    m, n = len(part), len(s)
    stack = []

    # attempt to match part against len(part) elements on top of stack
    def match_stack():
      temp = []
      idx = m-1
      while idx >= 0 and stack[-1] == part[idx]:
        temp.append(stack.pop())
        idx -= 1
      # mismatch found, revert contents of stack
      if idx != -1:
        while temp:
          stack.append(temp.pop())

    for i in range(n):
      stack.append(s[i])
      if len(stack) >= m:
        match_stack()

    return ''.join(stack)

