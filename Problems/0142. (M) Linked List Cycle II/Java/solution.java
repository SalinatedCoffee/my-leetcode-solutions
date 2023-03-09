public class Solution {
  public ListNode detectCycle(ListNode head) {
    // two pointers

    // sanity check
    if (head == null || head.next == null)
      return null;

    // cycle detection
    ListNode slow = head.next;
    ListNode fast = head.next != null? head.next.next : null;
    int slow_d = 1;
    while (slow != fast) {
      if (slow == null || fast == null)
        return null;
      slow = slow.next;
      fast = fast.next != null? fast.next.next : null;
      slow_d++;
    }

    // tail.next search
    slow = head;
    fast = head;
    for (int i = 0; i < slow_d; i++)
      fast = fast.next;
    while (slow != fast) {
      slow = slow.next;
      fast = fast.next;
    }
    return slow;
  }
}
