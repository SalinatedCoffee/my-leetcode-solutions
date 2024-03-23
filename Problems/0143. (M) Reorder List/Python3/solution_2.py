class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    # slow/fast pointers and partial list reversal

    # find first node of latter half of list
    slow, fast = head, head
    while fast:
      slow = slow.next
      fast = fast.next.next if fast.next else fast.next
    
    # reverse latter half
    prev, cur = None, slow
    while cur:
      temp = cur.next
      cur.next = prev
      prev = cur
      cur = temp
    
    # interleave the two halves
    cur = head
    while prev:
      t1, t2 = cur.next, prev.next
      cur.next = prev
      prev.next = t1
      cur, prev = t1, t2
    
    # properly terminate tail when list has odd length
    if cur:
      cur.next = None

