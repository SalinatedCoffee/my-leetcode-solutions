class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    # backtracking

    ret = []
    def recurse(cur, hanging, rem):
      # cur is string of parentheses up to current
      # hanging is number of open parentheses in cur
      # rem is number of remaining parentheses that can be opened
      if rem:
        recurse(cur+'(', hanging+1, rem-1)
      if hanging:
        recurse(cur+')', hanging-1, rem)
      if not hanging and not rem:
        ret.append(cur)
    
    recurse("", 0, n)

    return ret

