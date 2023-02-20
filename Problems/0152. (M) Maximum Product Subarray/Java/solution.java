class Solution {
  public int maxProduct(int[] nums) {
    // dp with memoization of min/max prods, based on kadane's algorithm

    int overall_max = nums[0];
    int running_max = nums[0];
    int running_min = nums[0];
    int prod_max, prod_min;
    for (int i=1; i<nums.length; i++) {
      // get product of current with previous running max/min prod
      prod_max = nums[i] * running_max;
      prod_min = nums[i] * running_min;
      // select max/min between current, prod min/max
      running_max = Math.max(Math.max(prod_max, prod_min), nums[i]);
      running_min = Math.min(Math.min(prod_max, prod_min), nums[i]);
      overall_max = Math.max(overall_max, running_max);
    }
    
    return overall_max;
  }
}
