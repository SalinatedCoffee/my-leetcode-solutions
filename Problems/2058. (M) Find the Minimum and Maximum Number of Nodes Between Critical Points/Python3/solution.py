class Solution:
  def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    # sliding window with greedy algorithm
    
    # find index of first critical point
    cur, cur_idx = head, 0
    last_idx = -1
    # look ahead 2 nodes
    while cur.next.next and last_idx == -1:
      m, h = cur.next, cur.next.next
      if (cur.val > m.val and h.val > m.val) \
        or (cur.val < m.val and h.val < m.val):
        last_idx = cur_idx + 1
      cur = cur.next
      cur_idx += 1
    first_idx = last_idx
    
    # greedily find minimum distance
    min_d = float('inf')
    while cur.next.next:
      m, h = cur.next, cur.next.next
      if (cur.val > m.val and h.val > m.val) \
        or (cur.val < m.val and h.val < m.val):
        min_d = min(min_d, cur_idx + 1 - last_idx)
        last_idx = cur_idx + 1
      cur = cur.next
      cur_idx += 1

    # greedily find maximum distance if at least 2 critical points exist
    return [min_d, last_idx - first_idx] if min_d != float('inf') else [-1, -1]

