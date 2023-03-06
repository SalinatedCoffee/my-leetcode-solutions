class Solution {
  public long countSubarrays(int[] nums, int minK, int maxK) {
    // multiple pointers, compute count on the fly

    // match return type
    long ret = 0;
    int min_idx, max_idx, l;
    // works for immutable data, integers are immutable in Java
    min_idx = max_idx = l = -1;

    for (int i = 0; i < nums.length; i++) {
      // number at index i is in range
      if (minK <= nums[i] && nums[i] <= maxK) {
        // min and max may be equal, so test for both
        if (nums[i] == minK)
          min_idx = i;
        if (nums[i] == maxK)
          max_idx = i;
      }
      else
        l = i;
      ret += Math.max(0, Math.min(min_idx, max_idx) - l);
    }
    return ret;
  }
}
