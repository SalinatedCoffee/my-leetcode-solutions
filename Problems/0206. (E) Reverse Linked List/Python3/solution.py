class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # single pass inplace reversal

    prev, cur = None, head
    while cur:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp

    return prev

