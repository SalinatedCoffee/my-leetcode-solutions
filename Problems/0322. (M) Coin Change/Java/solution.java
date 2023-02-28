class Solution {
  public int coinChange(int[] coins, int amount) {
    // bottom-up dynamic programming

    // trivial case
    if (amount == 0)
      return 0;

    // value of dp[i] is min number of coins that add up to i
    int[] dp = new int[amount+1];
    Arrays.fill(dp, amount+1);
    dp[0] = 0;

    for (int i = 1; i <= amount; i++) {
      // Java for-each syntax
      for (int denom : coins) {
        if (i >= denom) {
          dp[i] = Math.min(dp[i], dp[i-denom]+1);
        }
      }
    }
    
    return dp[amount] <= amount ? dp[amount] : -1;
  }
}
