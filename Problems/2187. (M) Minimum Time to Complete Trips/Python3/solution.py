class Solution:
  def minimumTime(self, time: List[int], totalTrips: int) -> int:
    # binary search

    # use shortest trip for upper bound
    min_trip = min(time)
    l, h = 1, min_trip*totalTrips
    prev = 0
    while l <= h:
      m = (l + h) // 2
      m_trips = 0
      for t in time:
        m_trips += m // t
      if totalTrips <= m_trips:
        # keep track of the last valid value
        prev = m
        h = m - 1
      else:
        l = m + 1
    
    return prev

