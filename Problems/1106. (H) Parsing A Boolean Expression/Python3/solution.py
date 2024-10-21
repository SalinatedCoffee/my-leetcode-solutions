class Solution:
  def parseBoolExpr(self, expression: str) -> bool:
    # stacks
    
    n = len(expression)
    # terms
    stack = []
    # operations
    opstack = []
    i = 0
    while i < n:
      c = expression[i]
      # push operation onto opstack
      if c in "&|!":
        opstack.append(c)
        stack.append('(')
        i += 1
      # push term onto stack
      elif c in 'tf':
        stack.append(True if c == 't' else False)
      # evaluate terms in current scope using operation
      elif c == ')':
        op = opstack[-1]
        cur = stack.pop()
        # if operation is NOT, this loop is not entered due to problem constraints
        while stack and stack[-1] != '(':
          match op:
            case '&':
              cur &= stack.pop()
            case '|':
              cur |= stack.pop()
        # remove dangling open parentheses from stack
        stack.pop()
        if op == '!':
          cur ^= True
        # push computed value back onto stack
        stack.append(cur)
        opstack.pop()
      i += 1

    return stack[-1]

