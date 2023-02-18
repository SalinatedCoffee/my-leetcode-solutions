class Solution {
  public TreeNode invertTree(TreeNode root) {
    // recursively swap subtrees
    if (root != null) {
      TreeNode left = invertTree(root.right);
      TreeNode right = invertTree(root.left);
      root.left = left;
      root.right = right;
    }
    return root;
  }
}
