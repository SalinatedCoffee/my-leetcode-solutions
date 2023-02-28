class Solution {
  Set<String> seen = new HashSet();
  Map<String,TreeNode> ret = new HashMap();

  public String recurse(TreeNode node) {
    // get string representations of subtrees recursively
    String l_str = (node.left != null) ? recurse(node.left) : "n";
    String r_str = (node.right != null) ? recurse(node.right) : "n";
    String in_str = l_str + Integer.toString(node.val) + r_str + ".";
    // no duplicate of subtree encountered previously
    if (!this.seen.contains(in_str))
      this.seen.add(in_str);
    // duplicate not yet added to result pool
    else if (!this.ret.containsKey(in_str))
      this.ret.put(in_str, node);

    return in_str;
  }
  public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
    // recursive DFS with hashing

    recurse(root);

    // return values only
    return new ArrayList<TreeNode>(this.ret.values());
  }
}
