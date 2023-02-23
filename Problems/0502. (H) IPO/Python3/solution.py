class Solution:
  def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
    # use sorted list with heap to store project pool

    # sort projects by capital
    cp_sorted = sorted(zip(capital, profits))
    # available projects at a given time
    avail_proj = []
    # index pointing to first unavailable project
    unavail = 0

    for i in range(k):
      # add all available projects to heap queue
      while unavail < len(cp_sorted) and w >= cp_sorted[unavail][0]:
        p = cp_sorted[unavail][1]
        # max heap hack for python heapqs
        heappush(avail_proj, -1*p)
        unavail += 1
      
      # no more projects available
      if not avail_proj:
        break

      # do available project
      p = heappop(avail_proj)
      w += -1*p

    return w

