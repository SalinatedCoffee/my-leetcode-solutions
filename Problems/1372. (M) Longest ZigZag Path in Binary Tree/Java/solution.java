class Solution {
  // recursive DFS

  int pathLength = 0;

  public int longestZigZag(TreeNode root) {
    // root has no parent, so direction does not matter
    dfs(root, false, 0);
    // dfs(root, true, 0); would also work
    return pathLength;
  }

  public void dfs(TreeNode node, boolean goLeft, int steps) {
    if (node == null)
      return;
    pathLength = Math.max(pathLength, steps);
    // node was right child
    if (goLeft) {
      dfs(node.left, false, ++steps);
      dfs(node.right, true, 1);
    }
    else {
      dfs(node.left, false, 1);
      dfs(node.right, true, ++steps);
    }
  }
}
