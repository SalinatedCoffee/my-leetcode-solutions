class Solution {
  public int rob(int[] nums) {
    // dynamic programming, zip two iterations into one

    // sanity check
    if (nums.length == 1)
      return nums[0];

    int res = -1;
    int temp;
    for (int j = 0; j < 2; j++) {
      int prev_2 = 0;
      int prev = nums[j];
      for (int i = j + 1; i < nums.length - 1 + j; i++) {
        temp = prev;
        prev = Math.max(prev_2+nums[i], prev);
        prev_2 = temp;
      }
      res = Math.max(res, prev);
    }
    return res;
  }
}
