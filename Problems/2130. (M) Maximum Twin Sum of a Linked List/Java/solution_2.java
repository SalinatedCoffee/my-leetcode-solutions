class Solution {
  public int pairSum(ListNode head) {
    // two pointers

    ListNode slow = head;
    ListNode fast = slow.next;
    while (fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
    }

    ListNode first = slow;
    ListNode second = slow.next;
    ListNode prev = null;
    ListNode cur = head;
    while (cur != slow) {
      ListNode temp = cur.next;
      cur.next = prev;
      prev = cur;
      cur = temp;
    }
    cur.next = prev;

    int ret = 0;
    while (first != null && second != null) {
      ret = Math.max(ret, first.val + second.val);
      first = first.next;
      second = second.next;
    }
    return ret;
  }
}
