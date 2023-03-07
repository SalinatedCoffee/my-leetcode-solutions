class Solution {
  public int[] countBits(int n) {
    // memoize previous results

    int[] ret = new int[n+1];
    for (int i = 0; i <= n; i++) {
      // bit manipulation faster than modulo or division
      ret[i] = ret[i>>1] + (i & 1);
    }
    return ret;
  }
}
