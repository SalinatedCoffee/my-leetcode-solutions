class Solution:
  def fractionAddition(self, expression: str) -> str:
    # regular expressions and math
    
    # parse fractions from expression string
    fractions = re.findall("[-+]*[0-9]+\/[0-9]+", expression)

    # compute sum of numerators for each denominator
    numerators = [0] * 11
    for frac in fractions:
      n, d = frac.split('/')
      numerators[int(d)] += int(n)
    
    # get list of denominators with non-zero numerator sum
    denominators = list(filter(lambda x: numerators[x] != 0, [i for i in range(1, 11)]))
    if not denominators:
      return "0/1"

    # compute LCM of all denominators with non-zero numerator sum
    cur = denominators[0]
    for i in range(1, len(denominators)):
      fac = gcd(cur, denominators[i])
      cur = (cur * denominators[i]) // fac
    
    # evaluate entire expression
    n = 0
    for d in denominators:
      n += numerators[d] * (cur // d)
    
    # simplify resulting fraction
    fac = gcd(n, cur)

    return str(n//fac) + '/' + str(cur//fac)

