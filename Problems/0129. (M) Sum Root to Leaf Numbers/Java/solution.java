class Solution {
  public int sumNumbers(TreeNode root) {
    // recursive DFS

    return recurse(root, 0);
  }

  private int recurse(TreeNode root, int total) {
    if (root == null)
      return 0;

    total *= 10;
    total += root.val;
    int lr_sum = recurse(root.left, total) + recurse(root.right, total);

    return lr_sum > 0 ? lr_sum : total;
  }
}
