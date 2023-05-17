class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    # two pointers

    slow = head
    fast = slow.next
    while fast.next:
      slow = slow.next
      fast = fast.next.next

    first = slow
    second = slow.next
    prev = None
    cur = head
    while cur != slow:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp
    cur.next = prev
    
    ret = 0
    while first and second:
      ret = max(ret, first.val + second.val)
      first = first.next
      second = second.next
    
    return ret

