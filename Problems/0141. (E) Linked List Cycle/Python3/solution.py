class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Floyd's tortoise and hare algorithm

    slow = fast = head
    while fast:
      slow = slow.next
      fast = fast.next
      if fast is None:
        break
      fast = fast.next
      if slow == fast:
        return True
        
    return False

