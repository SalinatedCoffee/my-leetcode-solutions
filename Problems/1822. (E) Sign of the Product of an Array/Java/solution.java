class Solution {
  public int arraySign(int[] nums) {
    // iteration

    boolean sign = true;
    for (int n: nums) {
      if (n == 0)
        return 0;
      if (n < 0)
        sign ^= true;
    }
    return sign ? 1 : -1;
  }
}
