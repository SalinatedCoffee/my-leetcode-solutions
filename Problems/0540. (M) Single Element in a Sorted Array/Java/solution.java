class Solution {
  public int singleNonDuplicate(int[] nums) {
    // modified binary search

    int lo = 0;
    int hi = nums.length - 1;
    while (lo < hi) {
      int mid = (hi-lo) / 2;
      // ensure left half has even length
      mid = mid % 2 == 1 ? mid : mid+1;
      mid += lo;
      // if last item in left is same as first in right
      if (nums[mid] == nums[mid+1])
        // take left half
        hi = mid-1;
      else
        lo = mid+1;
    }
    return nums[lo];
  }
}
