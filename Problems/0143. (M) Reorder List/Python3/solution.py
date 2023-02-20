class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    # store all nodes in queue
    # then first and last node pair is i-th and (n-i)-th nodes

    nodes = deque()
    cur = head
    while cur:
      nodes.append(cur)
      cur = cur.next
    
    prev_tail = head
    while len(nodes) > 1:
      left, right = nodes.popleft(), nodes.pop()
      prev_tail.next = left
      left.next = right
      prev_tail = right
    
    # if list has odd number of nodes
    if nodes:
      prev_tail.next = nodes.pop()
      prev_tail = prev_tail.next
    # tail node should point to None
    prev_tail.next = None

    # head is unchanged
    return head

