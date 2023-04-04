class Solution {
  public int partitionString(String s) {
    // greedy

    Set<Character> cur = new HashSet();
    int ret = 0;
    for (int i = 0; i < s.length(); i++) {
      if (!cur.contains(s.charAt(i)))
        cur.add(s.charAt(i));
      else {
        ret++;
        cur.clear();
        cur.add(s.charAt(i));
      }
    }
    return cur.size() > 0 ? ++ret : ret;
  }
}
