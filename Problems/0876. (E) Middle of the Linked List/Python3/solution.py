class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # slow/fast pointer

    s = f = head
    while f and f.next:
      s = s.next
      f = f.next.next if f.next else None

    return s

