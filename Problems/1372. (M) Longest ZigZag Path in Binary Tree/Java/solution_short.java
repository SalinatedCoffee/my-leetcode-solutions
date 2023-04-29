class Solution {
  // recursive DFS

  public int longestZigZag(TreeNode root) {
    return dfs(root, 0, 0);
  }

  public int dfs(TreeNode node, int l, int r) {
    return node == null ? 0 : Math.max(
      Math.max(l, r),
      Math.max(dfs(node.left, ++r, 0), dfs(node.right, 0, ++l)));
  }
}
