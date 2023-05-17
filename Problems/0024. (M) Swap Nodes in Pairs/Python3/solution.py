class Solution:
  def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # iteration

    if not head:
      return None

    l = head
    r = head.next
    # sentinel node
    ret = ListNode()
    prev = ret
    while l and r:
      temp = r.next
      prev.next = r
      prev = l
      r.next = l
      l = temp
      r = temp.next if temp else None
      
    if l:
      prev.next = l
    else:
      prev.next = None

    return ret.next

