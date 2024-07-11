class Solution:
  def reverseParentheses(self, s: str) -> str:
    # use pointers to jump around string

    n = len(s)
    # make first pass over s to pair indices of parentheses
    # portals[i] is index that should be jumped to at index i
    # if portals[i] == j, then portals[j] == i
    portals = {}
    parens = []
    for i, c in enumerate(s):
      match c:
        case '(':
          parens.append(i)
        case ')':
          j = parens.pop()
          portals[j] = i
          portals[i] = j
    
    # traverse s using 'jump' indices while building modified string
    ret = ""
    idx, direction = 0, 1
    while idx < n:
      # jump to parenthesis counterpart and reverse direction
      if s[idx] in "()":
        idx = portals[idx]
        direction ^= 1
      else:
        ret.append(s[idx])
      idx += 1 if direction else -1

    return ret

