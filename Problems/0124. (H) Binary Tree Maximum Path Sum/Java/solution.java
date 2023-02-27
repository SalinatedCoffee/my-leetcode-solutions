class Solution {
  // overall max path sum
  int max_sum = Integer.MIN_VALUE;

  public int recurse(TreeNode node) {
    // recursively get left and right path sums
    int left_sum = 0;
    int right_sum = 0;
    if (node.left != null)
      left_sum = recurse(node.left);
    if(node.right != null)
      right_sum = recurse(node.right);
    // see whether path sum in subtree rooted at node is larger than previous max
    this.max_sum = Math.max(this.max_sum, left_sum+node.val+right_sum);
    int ret = Math.max(left_sum+node.val, node.val+right_sum);
    return ret > 0 ? ret : 0;
  }


  public int maxPathSum(TreeNode root) {
    recurse(root);

    return this.max_sum;
  }
}
