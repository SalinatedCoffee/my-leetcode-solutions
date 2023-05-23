class Solution {
  // top-down dynamic programming (memoization)

  public int maxScore(int[] nums) {
    int[] memo = new int[(1 << nums.length)];
    Arrays.fill(memo, -1);
    return recurse(memo, 0, 0, nums);
  }

  private int recurse(int[] memo, int mask, int pairs_picked, int[] nums) {
    if (2 * pairs_picked == nums.length)
      return 0;
    if (memo[mask] != -1)
      return memo[mask];

    int max_score = 0;

    for (int i = 0; i < nums.length; i++) {
      for (int j = i+1; j < nums.length; j++) {
        if (((mask >> i) & 1) == 1 || ((mask >> j) & 1) == 1)
          continue;
        int new_mask = mask | (1 << i) | (1 << j);
        int cur_score = (pairs_picked + 1) * gcd(nums[i], nums[j]);
        int rem_score = recurse(memo, new_mask, pairs_picked+1, nums);
        max_score = Math.max(max_score, cur_score + rem_score);
      }
    }
    memo[mask] = max_score;
    return max_score;
  }

  private static int gcd(int x, int y) {
    while (y != 0) {
      int tX = x;
      x = y;
      y = tX % y;
    }
    return x;
  }
}
