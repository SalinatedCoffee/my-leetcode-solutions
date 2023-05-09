class Solution {
  public String predictPartyVictory(String senate) {
    // double queues

    int n = senate.length();
    Deque<Integer> r = new ArrayDeque();
    Deque<Integer> d = new ArrayDeque();
    for (int i = 0; i < n; i++) {
      if (senate.charAt(i) == 'R')
        r.add(i);
      else
        d.add(i);
    }

    while (r.size() > 0 && d.size() > 0) {
      int r_cur = r.remove();
      int d_cur = d.remove();
      if (r_cur > d_cur)
        d.add(d_cur+n);
      else
        r.add(r_cur+n);
    }
    return r.size() > 0 ? "Radiant" : "Dire";
  }
}
