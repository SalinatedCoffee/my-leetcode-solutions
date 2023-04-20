class Solution {
  public int widthOfBinaryTree(TreeNode root) {
    // iterative DFS with heap indices

    // max 'width' will fit in signed int, but heap indices may not
    // so save indices as long
    Map<Integer,long[]> widths = new HashMap();
    Deque<Triple<TreeNode,Integer,Long>> nodes = new ArrayDeque();
    // (node, depth, heap index)
    nodes.push(new Triple<TreeNode,Integer,Long>(root, 1, (long) 1));
    while (nodes.size() > 0) {
      Triple<TreeNode,Integer,Long> cur = nodes.pop();
      TreeNode c_node = cur.getA();
      int d = cur.getB();
      long i = cur.getC();
      if (widths.containsKey(d) == false)
        widths.put(d, new long[] {i, i});
      else {
        widths.get(d)[0] = Math.min(widths.get(d)[0], i);
        widths.get(d)[1] = Math.max(widths.get(d)[1], i);
      }
      if (c_node.left != null)
        nodes.push(new Triple<TreeNode,Integer,Long>(c_node.left, d+1, 2*i));
      if (c_node.right != null)
        nodes.push(new Triple<TreeNode,Integer,Long>(c_node.right, d+1, 2*i+1));
    }
    long ret = 0;
    for (long[] w: widths.values())
      ret = Math.max(ret, w[1]-w[0]+1);
    return (int) ret;
  }

  // absurd, yes
  class Triple<A,B,C> {
    A a;
    B b;
    C c;
    public Triple(A a, B b, C c) {
      this.a = a;
      this.b = b;
      this.c = c;
    }
    public A getA() {
      return this.a;
    }
    public B getB() {
      return this.b;
    }
    public C getC() {
      return this.c;
    }
  }
}
