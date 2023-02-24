class Solution {
  public int rob(int[] nums) {
    // dynamic programming

    // sanity check
    if (nums.length == 0)
      return 0;
    
    // dp[i] = maximum stolen up to nums[i-1]
    int[] dp = new int[nums.length+1];
    dp[1] = nums[0];

    for (int i = 1; i < nums.length; i++) {
      // either steal from current or skip
      dp[i+1] = Math.max(dp[i-1]+nums[i], dp[i]);
    }
    
    return dp[nums.length];
  }
}
