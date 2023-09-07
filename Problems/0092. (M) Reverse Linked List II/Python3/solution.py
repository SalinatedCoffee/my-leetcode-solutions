class Solution:
  def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    # 1-pass with multiple pointers

    # 'bordering' nodes in untouched sections
    l_tail, r_head = None, None
    # tail / head nodes of reversed section
    rev_tail, rev_head = None, None

    # walk list up to last node in left untouched section
    cur = head
    for _ in range(left-1):
      l_tail = cur
      cur = cur.next
    rev_tail = cur
    # walk list up to head of reversed section while reversing list
    prev = cur
    for i in range(right-left+1):
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp
    # reconnect sections
    r_head = cur
    rev_head = prev
    if l_tail:
      l_tail.next = rev_head
    rev_tail.next = r_head

    # check if entire list has been reversed
    return head if rev_tail is not head else rev_head

