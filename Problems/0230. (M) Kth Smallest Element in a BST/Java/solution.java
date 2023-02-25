class Solution {
  public int kthSmallest(TreeNode root, int k) {
    // inorder traversal with counter updates

    Deque<TreeNode> nodes = new ArrayDeque();
    TreeNode cur = root;
    // iterative traversal
    while (true) {
      if (cur != null) {
        nodes.push(cur);
        cur = cur.left;
      }
      else if (nodes.size() != 0) {
        cur = nodes.pop();
        // check and update counter appropriately
        if (k == 1)
          return cur.val;
        k--;
        cur = cur.right;
      }
      else
        break;
    }
    // this line will never run given constraints on number of nodes and k
    return -1;
  }
}
