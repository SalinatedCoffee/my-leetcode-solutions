class Solution {
  public int searchInsert(int[] nums, int target) {
    // binary search

    int lo = 0;
    int mid = 0;
    // nums is primitive array, use .length
    int hi = nums.length - 1;
    while (lo <= hi) {
      // no implicit type conversion on division
      mid = lo + (hi-lo) / 2;
      if (nums[mid] == target)
        return mid;
      else if (nums[mid] > target)
        hi = mid - 1;
      else
        lo = mid + 1;
    }
    return lo;
  }
}
