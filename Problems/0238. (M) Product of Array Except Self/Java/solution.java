class Solution {
  public int[] productExceptSelf(int[] nums) {
    // dynamic programming, precompute product in one direction

    // compute product of prefix in normal direction
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    for (int i = 1; i < nums.length; i++)
      dp[i] = nums[i] * dp[i-1];
    
    int[] res = new int[nums.length];
    // compute product of prefix in reverse while computing desired value
    int rev_prod = 1;
    for (int i = nums.length-1; i > 0; i--) {
      res[i] = dp[i-1] * rev_prod;
      rev_prod *= nums[i];
    }
    res[0] = rev_prod;

    return res;
  }
}
