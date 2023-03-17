class Solution {
  public ListNode mergeKLists(ListNode[] lists) {
    // priority queue

    // Java priority queues tiebreaks arbitrairily
    // Use first value of pair as compare predicate
    Queue<Pair<Integer,ListNode>> heads = 
      new PriorityQueue<>(Comparator.comparing(Pair::getKey));

    for (ListNode head: lists) {
      if (head != null)
        heads.add(new Pair<Integer,ListNode>(head.val, head));
    }

    // sanity check
    if (heads.size() == 0)
      return null;

    ListNode ret = heads.poll().getValue();
    ListNode prev = ret;
    if (ret.next != null)
      heads.add(new Pair<Integer,ListNode>(ret.next.val, ret.next));

    while (heads.size() > 0) {
      ListNode cur = heads.poll().getValue();
      prev.next = cur;
      prev = prev.next;
      // add next node if cur wasn't tail
      if (cur.next != null)
        heads.add(new Pair<Integer,ListNode>(cur.next.val, cur.next));
    }
    return ret;
  }
}
