class Solution:
  def reverseParentheses(self, s: str) -> str:
    # simulation using stack

    stack = []
    # preappend empty string if s doesn't start with open parenthesis
    if s[0] != '(':
     stack.append("")

    for c in s:
      match c:
        case '(':
          stack.append("")
        case ')':
          rev = stack.pop()[::-1]
          if len(stack):
            stack[-1] += rev
          else:
            stack.append(rev)
        case _:
          stack[-1] += c

    return stack[0]

