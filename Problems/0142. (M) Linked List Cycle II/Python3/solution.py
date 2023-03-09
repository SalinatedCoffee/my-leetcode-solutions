class Solution:
  def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # two pointers

    # sanity check
    if not head or not head.next:
      return None
    
    # cycle detection
    slow = head.next
    fast = head.next.next
    slow_d = 1
    while slow != fast:
      if not slow or not fast:
        return None
      slow = slow.next
      fast = fast.next.next if fast.next else None
      slow_d += 1
    
    # tail.next search
    slow = fast = head
    for i in range(slow_d):
      fast = fast.next
    while (slow != fast):
      slow = slow.next
      fast = fast.next

    return slow

