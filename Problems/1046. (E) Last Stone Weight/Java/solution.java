class Solution {
  public int lastStoneWeight(int[] stones) {
    // heap queue

    // Java pqueues also use min heaps as default, use max heap instead
    Queue<Integer> hq = new PriorityQueue(Collections.reverseOrder());
    for (int i: stones)
      hq.add(i);

    while (hq.size() > 1) {
      int y = hq.poll();
      int x = hq.poll();
      if (x == y)
        continue;
      hq.add(y-x);
    }
    return hq.size() == 0 ? 0 : hq.poll();
  }
}
