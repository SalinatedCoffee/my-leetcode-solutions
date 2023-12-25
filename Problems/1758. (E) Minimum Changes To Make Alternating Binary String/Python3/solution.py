class Solution:
  def minOperations(self, s: str) -> int:
    # math

    n = len(s)
    ones = [0,0]
    for i in range(n):
      if s[i] == '1':
        ones[i%2] += 1

    return min(n // 2 - ones[1] + ones[0], n // 2 + n % 2 - ones[0] + ones[1])

