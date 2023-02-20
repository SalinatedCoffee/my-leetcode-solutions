class Solution {
  public void reorderList(ListNode head) {
    // reverse the right half first, then interleave
    
    // double pointer at different speeds
    // slow points to first node of right half
    ListNode slow = head;
    ListNode fast = head;
    while (fast != null) {
      slow = slow.next;
      if (fast.next == null)
        break;
      fast = fast.next.next;
    }

    // reverse right half
    ListNode cur = slow;
    ListNode prev = null;
    ListNode temp = null;
    while (cur != null) {
      temp = cur.next;
      cur.next = prev;
      prev = cur;
      cur = temp;
    }

    // right half doesn't exist
    if (prev == null)
      return;
    
    // interleave left and right halves
    ListNode cur_l = head;
    ListNode cur_r = prev;
    ListNode temp_l, temp_r;
    while (cur_r != null) {
      temp_l = cur_l.next;
      temp_r = cur_r.next;
      cur_l.next = cur_r;
      cur_l = temp_l;
      cur_r.next = cur_l;
      cur_r = temp_r;
    }

    // if ll is odd length, terminate ll properly
    if (cur_l != null)
      cur_l.next = null;
  }
}
