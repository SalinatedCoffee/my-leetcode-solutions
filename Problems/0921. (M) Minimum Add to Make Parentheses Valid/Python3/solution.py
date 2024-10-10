class Solution:
  def minAddToMakeValid(self, s: str) -> int:
    # simulated stacks

    # number of hanging open and close parentheses
    l, r = 0, 0
    for c in s:
      match c:
        case '(':
          l += 1
        case ')':
          r += 0 if l else 1
          l -= 1 if l else 0

    return l + r

