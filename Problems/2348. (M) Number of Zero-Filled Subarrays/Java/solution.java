class Solution {
  public long zeroFilledSubarray(int[] nums) {
    // iterate while counting zeros

    long run = 0;
    long ret = 0;

    for (int n: nums) {
      if (n == 0)
        run += 1;
      else if (run > 0) {
        // Gaussian sum
        ret += run * (run+1) / 2;
        run = 0;
      }
    }
    // count last run of zeros
    return run > 0 ? ret + (run * (run+1) / 2) : ret;
  }
}
