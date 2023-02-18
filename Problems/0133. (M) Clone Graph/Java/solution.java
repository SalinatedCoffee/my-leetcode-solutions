class Solution {
  public Node cloneGraph(Node node) {
    // BFS, clone visited nodes

    // sanity check
    if (node == null)
      return null;

    // queue for BFS
    ArrayDeque<Node> nodes = new ArrayDeque<Node>();
    nodes.push(node);
    // hashmap (dictionary) for cloned nodes
    HashMap<Integer, Node> copied = new HashMap<Integer, Node>();
    copied.put(node.val, new Node(node.val));
    while (nodes.size() > 0) {
      Node cur = nodes.pop();
      // get size of current (original) node's adjacent list
      // condition in for loop gets *evaluated* every iteration
      // so can't: for (...; i < cur.neighbors.size(); ...)
      int adj_n = cur.neighbors.size();
      for (int i = 0; i < adj_n; i++) {
        // get adjacent (original) node
        Node adj = cur.neighbors.get(i);
        // adj. node not cloned yet
        if (!copied.containsKey(adj.val)) {
          copied.put(adj.val, new Node(adj.val));
          nodes.push(cur.neighbors.get(i));
        }
        // add edge between cloned nodes
        copied.get(cur.val).neighbors.add(copied.get(adj.val));
      }
    }

    return copied.get(1);
  }
}
