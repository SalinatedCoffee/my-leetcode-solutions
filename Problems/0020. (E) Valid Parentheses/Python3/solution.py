class Solution:
  def isValid(self, s: str) -> bool:
    # stack

    stack = []
    for c in s:
      # store open parentheses in stack
      if c in '({[':
        stack.append(c)
      else:
        # if closed parentheses match against top of stack
        if not stack:
          return False
        m = stack.pop()
        # switch-case, supported in Python 3.10+
        match c:
          case ')':
            if m != '(': return False
          case '}':
            if m != '{': return False
          case ']':
            if m != '[': return False
    
    return not stack

