class Solution:
  def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
    # two min heaps

    heapify(pool_l := costs[:candidates])
    # there may be less than 2*candidates candidates
    # if so, assign remaining candidates to pool_h
    heapify(pool_h := costs[max(candidates, len(costs)-candidates):])
    l, h = candidates, len(costs) - candidates - 1
    ret = 0
    while k:
      # short-circuit if either pool is empty
      if not pool_h or pool_l and pool_l[0] <= pool_h[0]:
        ret += heappop(pool_l)
        if l <= h:
          heappush(pool_l, costs[l])
          l += 1
      else:
        ret += heappop(pool_h)
        if l <= h:
          heappush(pool_h, costs[h])
          h -= 1
      k -= 1

    return ret

