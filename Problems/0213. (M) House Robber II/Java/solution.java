class Solution {
  public int rob(int[] nums) {
    // dynamic programming, iterate two times

    // sanity check
    if (nums.length == 1)
      return nums[0];

    // dp variables for range [0, n-2]
    int odd_prev_2 = 0;
    int odd_prev = nums[0];
    // dp variables for range [1, n-1]
    int even_prev_2 = 0;
    int even_prev = nums[1];

    int temp;
    // iterate range [0, n-2]
    for (int i = 1; i < nums.length-1; i++) {
      temp = odd_prev;
      odd_prev = Math.max(odd_prev_2+nums[i], odd_prev);
      odd_prev_2 = temp;
    }
    // iterate range [1, n-1]
    for (int i = 2; i < nums.length; i++) {
      temp = even_prev;
      even_prev = Math.max(even_prev_2+nums[i], even_prev);
      even_prev_2 = temp;
    }

    return Math.max(odd_prev, even_prev);
  }
}
