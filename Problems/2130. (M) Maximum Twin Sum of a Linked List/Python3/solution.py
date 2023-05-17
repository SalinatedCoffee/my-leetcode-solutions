class Solution:
  def pairSum(self, head: Optional[ListNode]) -> int:
    # deque

    nodes = deque()
    cur = head
    while cur:
      nodes.append(cur)
      cur = cur.next
    ret = 0
    while nodes:
      cur = nodes.popleft().val + nodes.pop().val
      ret = max(ret, cur)
    
    return ret

