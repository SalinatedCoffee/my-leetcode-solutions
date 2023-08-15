class Solution:
  def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
    # two pointers

    l_head, r_head = ListNode(), ListNode()
    l_cur, r_cur = l_head, r_head

    cur = head
    while cur:
      if cur.val >= x:
        r_cur.next = cur
        r_cur = r_cur.next
      else:
        l_cur.next = cur
        l_cur = l_cur.next
      cur = cur.next
    
    r_cur.next = None
    l_cur.next = r_head.next
    
    return l_head.next

