class Solution {
  public void sortColors(int[] nums) {
    // 3-way partitioning

    int n = nums.length;
    int l = 0, m = 0, h = n-1;
    int temp = 0;

    while (m <= h) {
      switch (nums[m]) {
        case 0:
          temp = nums[l];
          nums[l] = nums[m];
          nums[m] = temp;
          l++;
          m++;
          break;
        case 1:
          m++;
          break;
        case 2:
          temp = nums[m];
          nums[m] = nums[h];
          nums[h] = temp;
          h--;
      }
    }
  }
}
