class Solution {
  public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
    // iterative BFS

    Map<String,List<Pair<String,Double>>> adj = new HashMap();
    for (int i = 0; i < equations.size(); i++) {
      if (!adj.containsKey(equations.get(i).get(0)))
        adj.put(equations.get(i).get(0), new ArrayList());
      if (!adj.containsKey(equations.get(i).get(1)))
        adj.put(equations.get(i).get(1), new ArrayList());
      adj.get(equations.get(i).get(0)).add(new Pair(equations.get(i).get(1), values[i]));
      adj.get(equations.get(i).get(1)).add(new Pair(equations.get(i).get(0), 1/values[i]));
    }

    double[] ret = new double[queries.size()];
    for (int i = 0; i < queries.size(); i++) {
      List<String> q = queries.get(i);
      double ans = -1;
      if (adj.containsKey(q.get(0)) && adj.containsKey(q.get(1))) {
        Deque<Pair<String,Double>> nodes = new ArrayDeque();
        nodes.add(new Pair(q.get(0), 1.0));
        Set<String> visited = new HashSet();
        while (nodes.size() > 0) {
          Pair<String,Double> cur = nodes.pollFirst();
          if (visited.contains(cur.getKey()) || !adj.containsKey(cur.getKey()))
            continue;
          if (cur.getKey().equals(q.get(1))) {
            ans = cur.getValue();
            break;
          }
          visited.add(cur.getKey());
          for (int j = 0; j < adj.get(cur.getKey()).size(); j++) {
            List<Pair<String,Double>> nxt = adj.get(cur.getKey());
            nodes.add(new Pair(nxt.get(j).getKey(), cur.getValue() * nxt.get(j).getValue()));
          }
        }
      }
      ret[i] = ans;
    }
    return ret;
  }
}
