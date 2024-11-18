class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    # sliding window

    n = len(code)
    res = [0] * n
    # handle edge case
    if k == 0:
      return res
    # specify where to store window sum depending on sign of k
    tgt = abs(k) if k < 0 else (n-1)
    k = abs(k)
    l, w_sum = 0, sum(code[:k])
    while l < n:
      res[tgt] = w_sum
      w_sum -= code[l]
      w_sum += code[(l+k)%n]
      l += 1
      tgt = (tgt+1)%n

    return res

