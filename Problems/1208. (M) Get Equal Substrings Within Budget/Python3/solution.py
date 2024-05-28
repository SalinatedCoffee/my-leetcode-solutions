class Solution:
  def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
    # sliding window

    n = len(s)
    # precompute cost of each letter pair
    cost = [0] * n
    for i in range(n):
      cost[i] = abs(ord(s[i]) - ord(t[i]))

    # find longest convertable substring under maxCost
    ret = 0
    l, cur = 0, 0
    for i in range(n):
      cur += cost[i]
      while cur > maxCost:
        cur -= cost[l]
        l += 1
      ret = max(ret, i - l + 1)

    return ret

