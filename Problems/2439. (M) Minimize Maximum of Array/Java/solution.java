class Solution {
  public int minimizeArrayValue(int[] nums) {
    // greedy

    long ret = 0;
    long p_sum = 0;
    for (int i = 0; i < nums.length; i++) {
      p_sum += nums[i];
      ret = Math.max(ret, (long) Math.ceil((double) p_sum/(i+1)));
    }
    return (int) ret;
  }
}
