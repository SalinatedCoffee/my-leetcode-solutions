class Solution {
  public boolean isSameTree(TreeNode p, TreeNode q) {
    // recursively compare nodes

    // base case, both nodes are null
    if (p == null && q == null)
      return true;
    // base case, only one node is null
    if (p == null || q == null)
      return false;
    // nodes match, recurse on subtrees
    if (p.val == q.val)
      return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    // base case, nodes do not match
    return false;
  }
}
