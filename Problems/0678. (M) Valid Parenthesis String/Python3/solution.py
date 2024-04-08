class Solution:
  def checkValidString(self, s: str) -> bool:
    # top-down dynamic programming (memoization)

    n = len(s)

    @cache
    def recurse(o, i):
      # returns validity of s[i:] where o unmatched open parentheses
      #   exist in s[:i]

      # base case
      if i == n:
        return False if o else True

      if s[i] == '(' and recurse(o+1, i+1):
        return True
      elif s[i] == '*':
        if (o and recurse(o-1, i+1)) or \
          recurse(o, i+1) or \
          recurse(o+1, i+1):
          return True
      elif s[i] == ')' and o and recurse(o-1, i+1):
        return True
      
      return False

    return recurse(0, 0)

