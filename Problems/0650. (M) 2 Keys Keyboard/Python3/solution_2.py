class Solution:
  def minSteps(self, n: int) -> int:
    # math (prime factorization)

    ret = 0
    d = 2
    while n > 1:
      while n % d == 0:
        ret += d
        n //= d
      d += 1

    return ret

