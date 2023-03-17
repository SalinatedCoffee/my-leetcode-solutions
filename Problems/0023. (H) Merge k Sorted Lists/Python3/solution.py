class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # priority queue

    heads = []
    # tiebreaker
    count = 0

    for head in lists:
      if head:
        heappush(heads, (head.val, count, head))
        count += 1

    # sanity check
    if not heads:
      return None
    
    _, _, ret = heappop(heads)
    prev = ret
    if ret.next:
      heappush(heads, (ret.next.val, count, ret.next))
      count += 1

    while heads:
      _, _, cur = heappop(heads)
      prev.next = cur
      prev = prev.next
      # add next node if cur wasn't tail
      if cur.next:
        heappush(heads, (cur.next.val, count, cur.next))
        count += 1
    
    return ret

