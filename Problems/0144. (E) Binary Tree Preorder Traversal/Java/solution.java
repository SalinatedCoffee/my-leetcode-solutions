class Solution {
  // NLR, recursive traversal
  ArrayList<Integer> preorder = new ArrayList<Integer>();

  public void recurse(TreeNode node) {
    preorder.add(node.val);
    if (node.left != null)
      recurse(node.left);
    if (node.right != null)
      recurse(node.right);
  }

  public List<Integer> preorderTraversal(TreeNode root) {
    if (root != null)
      recurse(root);
    return preorder;
  }
}
