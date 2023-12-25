class Solution:
  def minOperations(self, s: str) -> int:
    # math

    n = len(s)
    one = 0
    for i in range(n):
      if i % 2:
        if s[i] == '1':
          one += 1
      elif s[i] == '0':
        one += 1

    return min(one, n - one)

