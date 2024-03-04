class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # delayed pointer

    cur, tgt = head, head
    # advance lead pointer n nodes ahead
    for _ in range(n):
      cur = cur.next
    if cur is None:
      return head.next
    # start advancing both pointers until lead reaches tail
    while cur.next:
      cur, tgt = cur.next, tgt.next
    
    # remove target node and return head accordingly
    tgt.next = tgt.next.next if tgt.next else None

    return head

