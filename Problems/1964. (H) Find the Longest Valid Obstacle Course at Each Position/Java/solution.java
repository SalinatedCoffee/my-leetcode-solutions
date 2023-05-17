class Solution {
  // greedy with binary search

  private int bisectRight(int[] A, int target, int right) {
    if (right == 0)
      return 0;
    int left = 0;
    while (left < right) {
      int mid = left + (right - left) / 2;
      if (A[mid] <= target)
        left = mid + 1;
      else
        right = mid;
    }
    return left;
  }

  public int[] longestObstacleCourseAtEachPosition(int[] obstacles) {

    int n = obstacles.length;
    int ll = 0;
    int[] ret = new int[n];
    // lis[i] is smallest value of last obstacle in courses that are i long
    int[] lis = new int[n];

    for (int i = 0; i < n; i++) {
      int h = obstacles[i];
      int idx = bisectRight(lis, h, ll);
      if (idx == ll)
        ll++;
      lis[idx] = h;
      ret[i] = idx + 1;
    }
    return ret;
  }
}
