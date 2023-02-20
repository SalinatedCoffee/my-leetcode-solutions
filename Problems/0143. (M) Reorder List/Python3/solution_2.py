class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    # reverse the right half first, then interleave

    # double pointer at different speeds
    # slow points to first node in right half
    slow, fast = head, head
    while fast:
      slow = slow.next
      if fast.next is None:
        break
      fast = fast.next.next
    
    # reverse right half
    cur = slow
    prev = None
    while cur:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp
    
    # right half doesn't exist
    if prev is None:
      return head
    
    # interleave left and right halves
    cur_l, cur_r = head, prev
    while cur_r:
      temp_l, temp_r = cur_l.next, cur_r.next
      cur_l.next = cur_r
      cur_l = temp_l
      cur_r.next = cur_l
      cur_r = temp_r
    
    # if ll is odd length, terminate ll properly
    if cur_l:
      cur_l.next = None
    
    return head

