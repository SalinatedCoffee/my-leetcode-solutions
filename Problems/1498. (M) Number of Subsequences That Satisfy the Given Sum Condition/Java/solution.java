class Solution {
  public int numSubseq(int[] nums, int target) {
    // sort with two pointers

    Arrays.sort(nums);
    int l = 0;
    int h = nums.length - 1;
    int mod = 1_000_000_007;
    int ret = 0;

    // precompute powers of 2
    int[] pow = new int[nums.length];
    pow[0] = 1;
    for (int i = 1; i < nums.length; i++)
      pow[i] = (pow[i - 1] * 2) % mod;

    while (l <= h) {
      if (nums[l] + nums[h] > target)
        h--;
      else {
        ret += pow[h-l];
        ret %= mod;
        l++;
      }
    }
    return ret;
  }
}
