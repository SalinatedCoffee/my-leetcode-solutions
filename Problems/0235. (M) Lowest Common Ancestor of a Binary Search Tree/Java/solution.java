class Solution {
  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    // binary search tree, return first preorder node with value between p and q

    Deque<TreeNode> nodes = new ArrayDeque();
    int l = Math.min(p.val, q.val);
    int h = Math.max(p.val, q.val);
    nodes.push(root);
    // iterative preorder DFS
    while (nodes.size() > 0) {
      TreeNode cur = nodes.pop();
      if (l <= cur.val && cur.val <= h)
        return cur;
      if (cur.right != null)
        nodes.push(cur.right);
      if (cur.left != null)
        nodes.push(cur.left);
    }
    // this line will never execute given constraints on p and q
    return null;
  }
}
