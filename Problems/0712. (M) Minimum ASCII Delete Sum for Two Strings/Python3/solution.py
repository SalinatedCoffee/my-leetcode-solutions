class Solution:
  # top-down dynamic programming (memoization)

  def minimumDeleteSum(self, s1: str, s2: str) -> int:
    self._s1 = s1
    self._s2 = s2
    # preconvert characters into ASCII values
    self.os1 = [ord(c) for c in s1]
    self.os2 = [ord(c) for c in s2]

    return self.recurse(len(s1)-1, len(s2)-1)

  @cache
  def recurse(self, i, j):
    # return minimum cost to match s1[:i+1] and s2[:j+1]
    
    if i < 0 and j < 0:
      return 0
    if i < 0:
      return self.os2[j] + self.recurse(i, j-1)
    if j < 0:
      return self.os1[i] + self.recurse(i-1, j)
    if self._s1[i] == self._s2[j]:
      return self.recurse(i-1, j-1)

    cost = float('inf')
    cost = min(cost, self.os1[i] + self.recurse(i-1, j))
    cost = min(cost, self.os2[j] + self.recurse(i, j-1))

    return cost

