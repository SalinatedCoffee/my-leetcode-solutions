class Solution {
  public int maxDepth(TreeNode root) {
    // recursive DFS

    // sanity check
    if (root == null)
      return 0;

    // recurse on children
    int left = maxDepth(root.left);
    int right = maxDepth(root.right);

    // return size of larger subtree
    if (left > right)
      return left+1;
    else
      return right+1;
  }
}
