class Solution {
  // recursive DFS
  public int count(TreeNode root) {
    // recursively count number of nodes in tree
    if (root == null)
      return 0;
    return 1 + count(root.left) + count(root.right);
  }

  public boolean recurse(TreeNode node, int i, int n) {
    // recursively check if left and right subtrees are complete
    if (node == null)
      return true;
    if (i >= n)
      return false;
    return dfs(node.left, 2*i+1, n) &&
           dfs(node.right, 2*i+2, n);
  }

  public boolean isCompleteTree(TreeNode root) {
    return recurse(root, 0, count(root));
  }
}
