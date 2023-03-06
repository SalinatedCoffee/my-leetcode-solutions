class Solution {
  public int findKthPositive(int[] arr, int k) {
    // binary search based on number of missing integers at element

    int l = 0;
    int h = arr.length - 1;
    while (l <= h) {
      int m = (l + h) / 2;
      if (arr[m] - m - 1 < k)
        l = m + 1;
      else
        h = m - 1;
    }
    return l + k;
  }
}
