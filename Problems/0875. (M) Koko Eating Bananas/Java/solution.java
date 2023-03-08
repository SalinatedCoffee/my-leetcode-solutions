class Solution {
  public int minEatingSpeed(int[] piles, int h) {
    // binary search on eating speed

    int lo = 1;
    int hi = 0;
    for (int pile: piles)
      hi = Math.max(hi, pile);
    
    int prev = 0;
    while (lo <= hi) {
      int mid = (lo + hi) / 2;
      // hours at rate mid may overflow integer
      long mid_hours = 0;
      for (int pile: piles) {
        mid_hours += pile / mid;
        mid_hours += pile%mid>0 ? 1 : 0;
      }
      // implicit type conversion from int to long
      if (mid_hours > h)
        lo = mid + 1;
      else {
        prev = mid;
        hi = mid - 1;
      }
    }
    return prev;
  }
}
