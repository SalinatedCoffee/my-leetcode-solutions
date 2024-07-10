class Solution:
  def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # two pointers

    # sanity check
    if k == 1:
      return head

    sentinel = ListNode(-1, head)
    l, h = sentinel, sentinel
    while True:
      # at this point, both l and h points to tail of previous section
      i = 0
      while i < k and h:
        h = h.next
        i += 1
      # section is shorter than k
      if not h:
        # probably not needed, but disconnect sentinel node before returning
        ret = sentinel.next
        sentinel.next = None
        return ret
      # at this point, h points to tail of unmodified current section
      prev_tail = l
      next_head = h.next
      cur_tail = l.next
      cur_head = h
      # reverse section
      prev, cur = l.next, l.next.next
      while prev is not h:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
      # relink reversed section to list
      prev_tail.next = cur_head
      cur_tail.next = next_head
      l, h = cur_tail, cur_tail

    # this section is unreachable given problem constraints
    return head

