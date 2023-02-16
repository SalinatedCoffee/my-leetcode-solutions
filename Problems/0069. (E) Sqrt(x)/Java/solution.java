class Solution {
  public int mySqrt(int x) {
    // Newton's method, need to modify Python solution to avoid casting to long

    int start=1, end=x, floorRes=0;
    while (start <= end) {
      int mid = start + (end-start) / 2;

      if (mid <= x / mid ) {
        floorRes = mid;
        start = mid+1;
      }
      else {
        end = mid-1;
      }
    } 
    return floorRes;
  }
}
