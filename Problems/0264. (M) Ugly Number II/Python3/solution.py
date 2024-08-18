class Solution:
  def nthUglyNumber(self, n: int) -> int:
    # heap and set

    FACTORS = [2, 3, 5]
    heap = [1]
    seen = set([1])
    cur = 1
    for _ in range(n):
      cur = heappop(heap)
      for factor in FACTORS:
        nxt = cur * factor
        if nxt not in seen:
          seen.add(nxt)
          heappush(heap, nxt)

    return cur

