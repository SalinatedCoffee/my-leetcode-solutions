class Solution {
  public boolean dfs(TreeNode node, Deque<TreeNode> path, int tgt) {
    // recursively build path from node to tgt

    if (node == null)
      return false;
    path.push(node);
    if (node.val == tgt)
      return true;
    if (dfs(node.left, path, tgt) || dfs(node.right, path, tgt))
      return true;
    path.pop();
    return false;
  }

  public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
    // get paths from root to p and q then compare

    // get paths from root to p and q
    Deque<TreeNode> path_p = new LinkedList();
    Deque<TreeNode> path_q = new LinkedList();
    dfs(root, path_p, p.val);
    dfs(root, path_q, q.val);
    // for some weird reason Java Deque push/pop adds/removes left item in stack
    // so reverse
    Iterator<TreeNode> it_p = path_p.descendingIterator();
    Iterator<TreeNode> it_q = path_q.descendingIterator();

    TreeNode ret = null;
    // compare both paths
    while (it_p.hasNext() && it_q.hasNext()) {
      TreeNode n_p = it_p.next();
      TreeNode n_q = it_q.next();
      if (n_p == n_q)
        ret = n_p;
      else
        return ret;
    }
    return ret;
  }
}
