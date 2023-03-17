class Solution {
  // recursive solution
  public TreeNode sortedArrayToBST(int[] nums) {
    return recurse(nums, 0, nums.length-1);
  }
  
  private TreeNode recurse(int[] nums, int l, int h) {
    int arr_len = h - l;
    int arr_mid = (l + h) / 2;

    if (arr_len < 0)
      return null;
    
    // recursively generate left and right subtrees
    TreeNode left = recurse(nums, l, arr_mid-1);
    TreeNode right = recurse(nums, arr_mid+1, h);
    return new TreeNode(nums[arr_mid], left, right);
  }
}
