class Solution {
  public long minimumTime(int[] time, int totalTrips) {
    // binary search

    // use shortest trip for upper bound
    // min value not supported by Java arrays
    int min_trip = Integer.MAX_VALUE;
    for (int trip: time)
      min_trip = Math.min(min_trip, trip);
    // return type is long, returning prev
    // prev is dependent on l, h, m, so use long for those vars too
    long l = 1;
    long h = (long) min_trip * totalTrips;
    long prev = 0;
    while (l <= h) {
      long m = (l + h) / 2;
      long m_trips = 0;
      for (int trip: time)
        m_trips += (m / trip);
      if (totalTrips <= m_trips) {
        // keep track of the last valid value
        prev = m;
        h = m - 1;
      }
      else
        l = m + 1;
    }
    return prev;
  }
}
