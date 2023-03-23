class Solution {
  public boolean canPlaceFlowers(int[] flowerbed, int n) {
    // brute force (greedy)

    // sanity check
    if (n == 0)
      return true;

    int[] fb = Arrays.copyOf(flowerbed, flowerbed.length);
    int planted = 0;

    for (int i = 0; i < fb.length; i++) {
      if (fb[i] == 0) {
        // check left and right plots
        boolean l = i == 0 || fb[i-1] == 0 ? true : false;
        boolean r = i == fb.length-1 || fb[i+1] == 0 ? true : false;
        // plant if plot available
        if (l && r) {
          fb[i] = 1;
          planted++;
          if (planted >= n)
            return true;
        }
      }
    }
    return planted >= n;
  }
}
