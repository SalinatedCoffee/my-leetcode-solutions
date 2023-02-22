class Solution {
  public boolean valid(int cap, int days, int[] weights) {
    // check whether packages can be shipped with capacity cap

    int cargo = 0;
    int day = 1;
    for (int i = 0; i < weights.length; i++) {
      if (cargo + weights[i] > cap) {
        day += 1;
        cargo = weights[i];
      }
      else
        cargo += weights[i];
    }
    return day <= days;
  }
  public int shipWithinDays(int[] weights, int days) {
    // binary search on capacity

    // initial range of [max(weights), sum(weights)]
    int lo = -1;
    int hi = 0;
    for (int i = 0; i < weights.length; i++) {
      hi += weights[i];
      lo = Math.max(lo, weights[i]);
    }

    // binary search
    int prev_mid = 0;
    int mid = 0;
    while (lo <= hi) {
      mid = (hi - lo) / 2 + lo;
      if (valid(mid, days, weights)) {
        prev_mid = mid;
        hi = mid - 1;
      }
      else
        lo = mid + 1;
    }
    return prev_mid;
  }
}
