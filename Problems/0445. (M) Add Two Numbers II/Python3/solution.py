class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # linked list traversal with modulo

    l1_int, l2_int = 0, 0
    # get integer sum of linked lists
    cur = l1
    while cur:
      l1_int *= 10
      l1_int += cur.val
      cur = cur.next
    cur = l2
    while cur:
      l2_int *= 10
      l2_int += cur.val
      cur = cur.next
    tgt = l1_int + l2_int

    # convert integer back to linked list
    if not tgt:
      return ListNode(0)
    digits = floor(log10(tgt))
    head = ListNode()
    prev = head
    while digits >= 0:
      mod = 10 ** digits
      a = tgt // mod
      tgt %= mod
      digits -= 1
      prev.next = ListNode(a)
      prev = prev.next
    
    return head.next

