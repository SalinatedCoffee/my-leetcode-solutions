class Solution {
  public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
    // BFS traversal with list for each level

    List<List<Integer>> ret = new ArrayList();
    // sanity check
    if (root == null)
      return ret;
    
    // using Queue methods, declare as Queue instead of List
    Queue<Pair<TreeNode,Integer>> nodes = new LinkedList();
    nodes.add(new Pair<TreeNode,Integer>(root, 0));
    // going to retrieve elements via index anyway, just use list
    List<Integer> level = new ArrayList();
    boolean l2r = true;
    int prev_depth = 0;
    while (!nodes.isEmpty()) {
      Pair<TreeNode,Integer> cur = nodes.remove();
      // decompose Pair
      TreeNode node = cur.getKey();
      int depth = cur.getValue();
      if (prev_depth != depth) {
        prev_depth = depth;
        if (l2r)
          ret.add(level);
        else {
          // manually reverse list
          List<Integer> lv = new ArrayList();
          for (int i = level.size()-1; i >= 0; i--)
            lv.add(level.get(i));
          ret.add(lv);
        }
        l2r ^= true;
        level = new ArrayList();
      }
      level.add(node.val);
      if (node.left != null)
        nodes.add(new Pair<TreeNode,Integer>(node.left, depth+1));
      if (node.right != null)
        nodes.add(new Pair<TreeNode,Integer>(node.right, depth+1));
    }

    // last level doesn't trigger depth change, check manually
    if (level.size() > 0) {
      if (l2r)
        ret.add(level);
      else {
        List<Integer> lv = new ArrayList();
        for (int i = level.size()-1; i >= 0; i--)
          lv.add(level.get(i));
        ret.add(lv);
      }
    }
    
    return ret;
  }
}
