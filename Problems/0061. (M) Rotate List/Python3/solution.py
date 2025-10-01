class Solution:
  def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # linked list traversal

    # sanity check
    if head is None:
      return None
    # determine length of linked list
    n, prev, cur = 0, None, head
    while cur:
      n += 1
      prev, cur = cur, cur.next
    # keep track of original tail node
    tail = prev

    k %= n
    # sanity check
    if k == 0:
      return head
    k = n - k

    # traverse and splice linked list
    prev, cur = None, head
    for _ in range(k):
      prev, cur = cur, cur.next
    prev.next = None
    tail.next = head if head is not tail else None

    return cur

