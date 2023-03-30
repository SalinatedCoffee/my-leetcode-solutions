class Solution:
  def isScramble(self, s1, s2):
    # top-down dynamic programming (recursive memoization)

    memo = {}
    def recurse(s1, s2):
      # recursively check if s2 is scramble of s1
      if (s1, s2) in memo:
        return memo[(s1, s2)]
      if not sorted(s1) == sorted(s2):
        return False
      if len(s1) == 1:
        return True
      

      for i in range(1, len(s1)):
        # recurse on swap / no swap
        if recurse(s1[:i], s2[-i:]) and recurse(s1[i:], s2[:-i]) or \
           recurse(s1[:i], s2[:i]) and recurse(s1[i:], s2[i:]):
          memo[(s1, s2)] = True
          return True
      memo[(s1, s2)] = False
      return False
    return recurse(s1, s2)

