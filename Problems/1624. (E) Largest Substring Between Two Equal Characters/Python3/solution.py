class Solution:
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    # single pass
    
    n = len(s)
    mn, mx = [float('inf')] * 26, [-1] * 26
    for i in range(n):
      idx = ord(s[i]) - ord('a')
      mn[idx], mx[idx] = min(mn[idx], i), max(mx[idx], i)

    ret = -1
    for i, j in zip(mn, mx):
      if i != float('inf'):
        ret = max(ret, j - i - 1)

    return ret

