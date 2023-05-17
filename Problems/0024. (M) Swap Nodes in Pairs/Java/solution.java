class Solution {
  public ListNode swapPairs(ListNode head) {
    // iteration

    if (head == null)
      return null;
    
    ListNode l = head;
    ListNode r = head.next;
    // sentinel node
    ListNode ret = new ListNode();
    ListNode prev = ret;
    while (l != null && r != null) {
      ListNode temp = r.next;
      prev.next = r;
      prev = l;
      r.next = l;
      l = temp;
      r = temp != null ? temp.next : null;
    }

    if (l != null)
      prev.next = l;
    else
      prev.next = null;
    return ret.next;
  }
}
