class Solution {
  public int rob(int[] nums) {
    // dynamic programming

    // sanity check
    if (nums.length == 0)
      return 0;
    
    // max. stolen up to 2nd previous house
    int prev_2 = 0;
    // max. stolen up to previous house
    int prev = nums[0];

    int temp;
    for (int i = 1; i < nums.length; i++) {
      // either steal from current or skip
      temp = prev;
      prev = Math.max(prev_2+nums[i], prev);
      prev_2 = temp;
    }
    
    return prev;
  }
}
