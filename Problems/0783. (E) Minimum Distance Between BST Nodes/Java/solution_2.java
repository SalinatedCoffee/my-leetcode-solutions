class Solution {
  // inorder (LNR) to retrieve nodes in sorted order
  // compute min. diff during traversal

  int prev = -1;
  int min_diff = (int)Math.pow(10, 5)+1;

  public void recurse(TreeNode node) {
      if (node.left != null)
        recurse(node.left);
      if (prev != -1)
        min_diff = Math.min(min_diff, Math.abs(node.val-prev));
      prev = node.val;
      if (node.right != null)
        recurse(node.right);
  }

  public int minDiffInBST(TreeNode root) {
    recurse(root);

    return min_diff;
  }
}
