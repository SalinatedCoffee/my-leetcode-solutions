class Solution:
  def canChange(self, start: str, target: str) -> bool:
    # two pointers

    n = len(start)
    s, t = 0, 0

    while s < n or t < n:
      # advance both pointers to non-underscore character
      while s < n and start[s] == '_':
        s += 1
      while t < n and target[t] == '_':
        t += 1
      # if only one string has been entirely examined,
      # it is not possible to convert start to target
      if s == n or t == n:
        return s == n and t == n
      if start[s] != target[t] \
        or (start[s] == 'L' and s < t) \
        or (start[s] == 'R' and s > t):
        return False
      s += 1
      t += 1

    return True

