class Solution {
  public int pairSum(ListNode head) {
    // deque

    Deque<ListNode> nodes = new ArrayDeque();
    ListNode cur = head;
    while (cur != null) {
      nodes.add(cur);
      cur = cur.next;
    }
    int ret = 0;
    int cur_sum = 0;
    while (nodes.size() > 0) {
      cur_sum = nodes.removeFirst().val + nodes.removeLast().val;
      ret = Math.max(ret, cur_sum);
    }
    return ret;
  }
}
