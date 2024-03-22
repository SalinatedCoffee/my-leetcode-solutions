class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # partial reversal using slow/fast pointers
    
    # slow points to middle node if list has odd length
    # otherwise, points to first node of second half
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next if fast.next else fast.next
    
    # reverse second half of list
    cur = slow
    prev = None
    while cur:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp
    # compare halves
    cur = head
    while prev and cur:
      if prev.val != cur.val:
        return False
      prev, cur = prev.next, cur.next

    return True

