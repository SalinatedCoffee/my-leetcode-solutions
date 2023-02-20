class Solution {
  public void reorderList(ListNode head) {
    // store all nodes in queue
    // then first and last nodes are i-th and (n-i)-th nodes

    // removeFirst/Last are Deque interfaces
    Deque<ListNode> nodes = new ArrayDeque();
    ListNode cur = head;
    while (cur != null) {
      nodes.add(cur);
      cur = cur.next;
    }

    ListNode prev_tail = head;
    while (nodes.size() > 1) {
      ListNode left = nodes.removeFirst();
      ListNode right = nodes.removeLast();
      prev_tail.next = left;
      left.next = right;
      prev_tail = right;
    }

    // if list has odd number of nodes
    if (nodes.size() == 1) {
      prev_tail.next = nodes.remove();
      prev_tail = prev_tail.next;
    }
    // tail node should point to null
    prev_tail.next = null;
  }
}
