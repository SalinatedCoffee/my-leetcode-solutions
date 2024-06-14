class Solution:
  def diffWaysToCompute(self, expression: str) -> List[int]:
    # recursion

    # translate character to operation
    OPS = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y}
    # parse expression string into tokens of integers and operator characters
    val = 0
    expr = []
    for c in expression:
      if c in OPS:
        expr.append(val)
        expr.append(c)
        val = 0
      else:
        val *= 10
        val += int(c)
    expr.append(val)
    n = len(expr)

    def recurse(i, j):
      # recurse(i, j) returns list of values of all possible evaulations of
      #   expr[i:j+1] where expr[i] and expr[j] are integers
      # base cases
      if i == j:
        return [expr[i]]
      if j - i == 2:
        return [OPS[expr[i+1]](expr[i], expr[j])]
      # for each operator between indices i and j, recursively try all evaulations
      # for left and right side terms
      ret = []
      for k in range(i+1, j, 2):
        l, r = recurse(i, k-1), recurse(k+1, j)
        for a in l:
          for b in r:
            ret.append(OPS[expr[k]](a, b))

      return ret

    return recurse(0, n-1)

