class Solution {
  // inorder (LNR) to retrieve nodes in sorted order
  // generate inorder list of nodes and iterate across it

  ArrayList<Integer> inorder = new ArrayList<Integer>();

  public void recurse(TreeNode node) {
      if (node.left != null)
        recurse(node.left);
      inorder.add(node.val);
      if (node.right != null)
        recurse(node.right);
  }

  public int minDiffInBST(TreeNode root) {
    recurse(root);
    int min_diff = (int) Math.pow(10, 5)+1;
    for (int i = 1; i < inorder.size(); i++)
      min_diff = Math.min(min_diff, Math.abs(inorder.get(i)-inorder.get(i-1)));
    return min_diff;
  }
}
