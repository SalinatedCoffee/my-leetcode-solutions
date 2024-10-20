class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    # brute force

    s_prev = [0]
    while n:
      s = s_prev + [1] + list(reversed(list(map(lambda x: x^1, s_prev))))
      s_prev = s
      n -= 1

    return str(s_prev[k-1])

