class Solution {
  // recursive solution
  public boolean isSymmetric(TreeNode root) {
    return recurse(root.left, root.right);
  }

  private boolean recurse(TreeNode left, TreeNode right) {
    // base cases
    if (left == null && right == null)
      return true;
    if (left == null || right == null)
      return false;

    // check current pair and compare recursively
    return left.val == right.val &&
           recurse(left.left, right.right) &&
           recurse(left.right, right.left);
  }
}
