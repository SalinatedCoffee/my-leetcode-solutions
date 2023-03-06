class Solution {
  public int minJumps(int[] arr) {
    // bfs, use dictionary mapping value to indices

    Map<Integer,List<Integer>> v2i = new HashMap();
    for (int i = 0; i < arr.length; i++) {
      if (!v2i.containsKey(arr[i]))
        v2i.put(arr[i], new ArrayList());
      v2i.get(arr[i]).add(i);
    }

    Deque<Pair<Integer,Integer>> nodes = new ArrayDeque();
    Set<Integer> visited = new HashSet();
    nodes.add(new Pair<Integer,Integer>(0,0));
    while (nodes.size() != 0) {
      Pair<Integer,Integer> cur = nodes.removeFirst();
      int idx = cur.getKey();
      int jmp = cur.getValue();
      if (visited.contains(idx))
        continue;
      visited.add(idx);
      if (idx == arr.length-1)
        return jmp;
      if (v2i.containsKey(arr[idx])) {
        // Java for-each
        for (int i: v2i.get(arr[idx]))
          nodes.add(new Pair<Integer,Integer>(i,jmp+1));
        // no longer need to consider jumps between indices with value arr[idx]
        v2i.remove(arr[idx]);
      }
      if (idx != 0)
        nodes.add(new Pair<Integer,Integer>(idx-1,jmp+1));
      nodes.add(new Pair<Integer,Integer>(idx+1,jmp+1));
    }
    // this line should never execute given problem description
    return -1;
  }
}
