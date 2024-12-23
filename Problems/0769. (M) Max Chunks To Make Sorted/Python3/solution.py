class Solution:
  def maxChunksToSorted(self, arr: List[int]) -> int:
    # prefix / suffix preprocessing

    n = len(arr)
    # pre[i] is largest element in arr[:i+1]
    # suf[i] is smallest element in arr[i:]
    pre, suf = [0] * n, [0] * n
    cur = 0
    for i in range(n):
      cur = max(cur, arr[i])
      pre[i] = cur
    cur = float('inf')
    for i in range(n-1, -1, -1):
      cur = min(cur, arr[i])
      suf[i] = cur

    res = 0
    for i in range(n):
      if i == 0 or pre[i-1] < suf[i]:
        res += 1

    return res

