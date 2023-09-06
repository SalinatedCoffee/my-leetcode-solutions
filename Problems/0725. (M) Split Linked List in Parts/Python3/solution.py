class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    # 2-pass, split original list

    cur = head
    n = 0
    while cur:
      cur = cur.next
      n += 1
    
    size, r = n // k, n % k
    cur = head
    ret = []
    for i in range(k):
      p_head = cur
      for j in range(size + (1 if i < r else 0) - 1):
        cur = cur.next if cur is not None else None
      if cur:
        cur.next, cur = None, cur.next
      ret.append(p_head)

    return ret

